import pytest
# make sure there's an __init__.py in this test folder and that
# the test folder is in the same folder as the mini project content
from PumpkinMachine import PumpkinMachine, STAGE
from PumpkinMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
# this is an example test showing how to cascade fixtures to build up state


@pytest.fixture
def machine():
    pm = PumpkinMachine()
    return pm

# sample fixture, can delete if not using


@pytest.fixture
def first_order(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("done")
    machine.handle_pay(10000, "10000")
    return machine

# sample fixture, can delete if not using


@pytest.fixture
def second_order(first_order):
    first_order.handle_pumpkin_choice("Large Pumpkin")
    first_order.handle_face_stencil_choice("Spooky Face")
    first_order.handle_face_stencil_choice("Toothy Face")
    first_order.handle_face_stencil_choice("next")
    first_order.handle_extra_choice("LED Candle")
    first_order.handle_extra_choice("Dry Ice")
    first_order.handle_extra_choice("done")
    # machine.handle_pay(10000,"10000")
    return first_order

# sample test case, can delete if not using


def test_production_line(second_order):
    for j in second_order.pumpkins:
        print(second_order.inprogress_pumpkin)
        if j.name.lower() == second_order.inprogress_pumpkin[0].name.lower():
            print(f"Pumkin {j.name.lower()} matches in progress \
                {second_order.inprogress_pumpkin[0].name.lower()}")
            assert True
            return

    assert False

# add required test cases below

# Test that selecting a pumpkin is required as the first choice
def test_pumpkin_must_be_first_selection(machine):
    with pytest.raises(InvalidStageException) as exc_info:
        machine.handle_face_stencil_choice("Happy Face")
    assert "You must choose a pumpkin first." in str(exc_info.value)


# Test that you can only add face stencils if they're in stock
@pytest.mark.parametrize("pumpkin_choice, valid_face_stencil, invalid_face_stencil", [
    ("Mini Pumpkin", "Happy Face", "Unavailable Face Stencil"),  # Valid pumpkin and valid face stencil
    ("Small Pumpkin", "Scream Face", "Invalid Face Stencil"),  # Valid pumpkin and invalid face stencil
])
def test_add_face_stencils_in_stock(pumpkin_choice, valid_face_stencil, invalid_face_stencil):
    machine = PumpkinMachine()

    # Make a valid pumpkin choice
    machine.handle_pumpkin_choice(pumpkin_choice)

    # Add a face stencil that is in stock (valid)
    machine.handle_face_stencil_choice(valid_face_stencil)

    # Verify that the valid face stencil was added
    assert valid_face_stencil in [item.name for item in machine.inprogress_pumpkin]

    # Try to add a face stencil that is not in stock (invalid)
    with pytest.raises(Exception):
        machine.handle_face_stencil_choice(invalid_face_stencil)

    # Verify that the invalid face stencil was not added
    assert invalid_face_stencil not in [item.name for item in machine.inprogress_pumpkin]


test_data = [
    ("Mini Pumpkin", "Happy Face", "LED Candle"),
    ("Small Pumpkin", "Happy Face", "Sticker Pack"),
    ("Medium Pumpkin", "Happy Face", "Paint Kit"),
    ("Large Pumpkin", "Happy Face", "Dry Ice"),
    ("Medium Pumpkin", "Happy Face", "Googly Eyes"),
    ("Large Pumpkin", "Happy Face", "Glitter"),
    ("Small Pumpkin", "Happy Face", "LED Candle"),
    ("Mini Pumpkin", "Happy Face", "Sticker Pack"),
    ("Medium Pumpkin", "Happy Face", "Dry Ice"),
    ("Large Pumpkin", "Happy Face", "Paint Kit"),
]
@pytest.mark.parametrize("pumpkin_choice, face_stencil, extra", test_data)
def test_add_instock_extras(pumpkin_choice, face_stencil, extra):
    machine = PumpkinMachine()
    machine.handle_pumpkin_choice(pumpkin_choice)
    machine.handle_face_stencil_choice(face_stencil)
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice(extra)

    machine.handle_pumpkin_choice(pumpkin_choice)

