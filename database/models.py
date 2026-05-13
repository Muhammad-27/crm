from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# 1. Foydalanuvchilar jadvali
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    role = Column(String, default="student") # rollar: teacher, assistant, student
    
    # Bog'lanishlar
    attendances = relationship("Attendance", back_populates="student")
    tasks = relationship("Task", back_populates="student")
    payments = relationship("Payment", back_populates="student")

# 2. Davomat jadvali
class Attendance(Base):
    __tablename__ = 'attendance'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('users.id'))
    date = Column(Date, nullable=False)
    is_present = Column(Boolean, default=False)
    
    student = relationship("User", back_populates="attendances")

# 3. Topshiriqlar (Speaking, Essential)
class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('users.id'))
    task_type = Column(String) # 'speaking' yoki 'essential'
    score = Column(String) # Bahosi yoki darajasi
    date = Column(Date, nullable=False)
    
    student = relationship("User", back_populates="tasks")

# 4. To'lovlar jadvali
class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Integer)
    month = Column(String) # Masalan: '2023-10'
    is_paid = Column(Boolean, default=False)
    
    student = relationship("User", back_populates="payments")
    # 5. O'qituvchi paneli orqali qo'shilgan o'quvchilar jadvali
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    teacher_telegram_id = Column(String, index=True) # O'quvchini qo'shgan o'qituvchining Telegram ID si
    full_name = Column(String, nullable=False)
    phone = Column(String)
    fee = Column(Integer)
    is_paid = Column(Boolean, default=False)