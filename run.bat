@echo off
echo Starting Transli Backend...
start "Transli Backend" cmd /k "cd backend && venv\Scripts\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8000"

echo Starting Transli Frontend...
start "Transli Frontend" cmd /k "cd frontend && npm run dev"

echo.
echo Transli has been launched!
echo Backend: http://127.0.0.1:8000
echo Frontend: http://localhost:5173
echo.
pause
