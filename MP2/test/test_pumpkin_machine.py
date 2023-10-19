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


# add required test cases below

"""Name: Bhavya Shah; UCID: bs635; Date: 19 October, 2023"""
# Test that selecting a pumpkin is required as the first choice
def test_pumpkin_must_be_first_selection(machine):
    with pytest.raises(InvalidStageException) as exc_info:
        machine.handle_face_stencil_choice("Happy Face")
    
    with pytest.raises(InvalidStageException) as exc_info:
        machine.handle_extra_choice("LED Candle")

"""Name: Bhavya Shah; UCID: bs635; Date: 19 October, 2023"""
@pytest.fixture
def change_quantity():
    pm = PumpkinMachine()
    for face_stencils in pm.face_stencils:
        if face_stencils.name == "Spooky Face":
            face_stencils.quantity = 1    
    for extras in pm.extras:
        if extras.name == "Glitter":
            extras.quantity = 2
    return pm

def test_face_stencil_instock(change_quantity):
    change_quantity.handle_pumpkin_choice("Small Pumpkin")
    change_quantity.handle_face_stencil_choice("Spooky Face")
    with pytest.raises(OutOfStockException) as exc_info:
        change_quantity.handle_face_stencil_choice("Spooky Face")


def test_extras_instock(change_quantity):
    change_quantity.handle_pumpkin_choice("Small Pumpkin")
    change_quantity.handle_face_stencil_choice("Spooky Face")
    change_quantity.handle_face_stencil_choice("next")
    change_quantity.handle_extra_choice("Glitter")
    change_quantity.handle_extra_choice("Glitter")
    with pytest.raises(OutOfStockException) as exc_info:
        change_quantity.handle_extra_choice("Glitter")


"""Name: Bhavya Shah; UCID: bs635; Date: 19 October, 2023"""
def test_upto_3_face_stencils(machine):
    machine.handle_pumpkin_choice("Small Pumpkin")
    machine.handle_face_stencil_choice("Scream Face")
    machine.handle_face_stencil_choice("Toothy Face")
    machine.handle_face_stencil_choice("Happy Face")
    with pytest.raises(ExceededRemainingChoicesException) as exc_info:
        machine.handle_face_stencil_choice("Spooky Face")


"""Name: Bhavya Shah; UCID: bs635; Date: 19 October, 2023"""
def test_upto_3_extras(machine):
    machine.handle_pumpkin_choice("Small Pumpkin")
    machine.handle_face_stencil_choice("Scream Face")
    machine.handle_face_stencil_choice("Toothy Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("Paint Kit")
    machine.handle_extra_choice("LED Candle")
    machine.handle_extra_choice("Paint Kit")
    with pytest.raises(ExceededRemainingChoicesException) as exc_info:
        machine.handle_extra_choice("Dry Ice")


"""Name: Bhavya Shah; UCID: bs635; Date: 19 October, 2023"""
test_data = [
    ("Mini Pumpkin", ["Spooky Face","next"], ["Glitter", "done"], 2.25),    
    ("Small Pumpkin", ["Happy Face", "next"], ["done"], 3.00),
    ("Medium Pumpkin", ["Toothy Face", "Spooky Face", "next"], ["Spooky Sound Effects", "Googly Eyes", "done"], 6.00),      
]
@pytest.mark.parametrize("pumpkin_choice, face_stencil_choice, extras_choice, expected_cost", test_data)
def test_cost(pumpkin_choice, face_stencil_choice, extras_choice, expected_cost):
    total = 0
    pm = PumpkinMachine()
    pm.handle_pumpkin_choice(pumpkin_choice)
    for face_stencil in face_stencil_choice:
        pm.handle_face_stencil_choice(face_stencil)

    for extra in extras_choice:
        pm.handle_extra_choice(extra)
    total = pm.calculate_cost()
    assert total == expected_cost
    pm.reset()


"""Name: Bhavya Shah; UCID: bs635; Date: 19 October, 2023"""
total_sales_data = [
    ("Mini Pumpkin", ["Spooky Face", "next"], ["Glitter", "done"], 2.25),
    ("Small Pumpkin", ["Happy Face", "next"], ["done"], 3.00),
    ("Medium Pumpkin", ["Toothy Face", "Spooky Face", "next"], ["Spooky Sound Effects", "Googly Eyes", "done"], 6.00),
]

@pytest.mark.parametrize("pumpkin_choice, face_stencil_choice, extras_choice, expected_cost", total_sales_data)
def test_total_sales(pumpkin_choice, face_stencil_choice, extras_choice, expected_cost):
    pm = PumpkinMachine()

    initial_expected_cost = pm.calculate_cost()

    pm.handle_pumpkin_choice(pumpkin_choice)
    for face_stencil in face_stencil_choice:
        pm.handle_face_stencil_choice(face_stencil)
    for extra in extras_choice:
        pm.handle_extra_choice(extra)

    expected_total_sales = initial_expected_cost + expected_cost
    
    # Handle payment with the expected total cost to update total_sales
    pm.handle_pay(expected_total_sales, f"${expected_total_sales:.2f}")
    assert pm.total_sales == expected_total_sales



"""Name: Bhavya Shah; UCID: bs635; Date: 19 October, 2023"""
total_products_data = [
    ("Mini Pumpkin", ["Spooky Face", "next"], ["Glitter", "done"]),
    ("Small Pumpkin", ["Happy Face", "next"], ["done"]),
    ("Medium Pumpkin", ["Toothy Face", "Spooky Face", "next"], ["Spooky Sound Effects", "Googly Eyes", "done"]),
    ("Large Pumpkin", ["Scream Face", "next"], ["Small Candle", "done"]),
    ("Mini Pumpkin", ["Happy Face", "next"], ["Sticker Pack", "LED Candle", "done"]),
    ("Small Pumpkin", ["Happy Face", "next"], ["Glitter", "done"]),
    ("Large Pumpkin", ["Scream Face", "next"], ["Small Candle", "done"]),
]
@pytest.mark.parametrize("pumpkin_choice, face_stencil_choice, extras_choice", total_products_data)
def test_total_products(pumpkin_choice, face_stencil_choice, extras_choice):
    pm = PumpkinMachine()
    expected_total_products = 0

    pm.handle_pumpkin_choice(pumpkin_choice)
    for face_stencil in face_stencil_choice:
        pm.handle_face_stencil_choice(face_stencil)
    for extra in extras_choice:
        pm.handle_extra_choice(extra)
    expected_total_products += 1  # Increment total products for the purchase
    pm.handle_pay(pm.calculate_cost(), f"${pm.calculate_cost():.2f}")

    assert pm.total_products == expected_total_products




