from app import app
from models import db, User, Role

with app.app_context():
    db.create_all()

    # Criar roles e usuários de exemplo
    admin_role = Role(name='admin')
    user_role = Role(name='user')
    db.session.add(admin_role)
    db.session.add(user_role)
    db.session.commit()

    admin_user = User(username='admin', password='admin')
    admin_user.roles.append(admin_role)
    db.session.add(admin_user)
    db.session.commit()
