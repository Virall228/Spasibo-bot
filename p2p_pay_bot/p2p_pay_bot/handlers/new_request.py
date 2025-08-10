from aiogram import Router, types, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()
requests = []

class RequestState(StatesGroup):
    waiting_for_title = State()
    waiting_for_amount = State()
    waiting_for_wallet = State()

@router.message(commands=["new_request"])
async def cmd_new_request(message: types.Message, state: FSMContext):
    await message.answer("📄 Введите название услуги (например: Spotify, Steam и т.д.):")
    await state.set_state(RequestState.waiting_for_title)

@router.message(RequestState.waiting_for_title, F.text)
async def process_title(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer("💶 Введите сумму (в евро):")
    await state.set_state(RequestState.waiting_for_amount)

@router.message(RequestState.waiting_for_amount, F.text)
async def process_amount(message: types.Message, state: FSMContext):
    try:
        amount = float(message.text.replace(",", "."))
    except ValueError:
        return await message.answer("❌ Пожалуйста, введите корректную сумму (число).")
    await state.update_data(amount=amount)
    await message.answer("🔐 Введите ваш TON кошелёк для получения оплаты:")
    await state.set_state(RequestState.waiting_for_wallet)

@router.message(RequestState.waiting_for_wallet, F.text)
async def process_wallet(message: types.Message, state: FSMContext):
    data = await state.update_data(wallet=message.text)
    user_data = await state.get_data()
    requests.append({
        "user_id": message.from_user.id,
        "username": message.from_user.username,
        "title": user_data["title"],
        "amount": user_data["amount"],
        "wallet": user_data["wallet"]
    })
    await message.answer("✅ Заявка успешно создана и добавлена в маркетплейс!")
    await state.clear()