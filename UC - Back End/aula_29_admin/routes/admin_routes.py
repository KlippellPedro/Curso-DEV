from flask import Blueprint, render_template, request, redirect, url_for
from models.user_model import *
from utils.decorators import admin_required
from werkzeug.security import generate_password_hash

bp = Blueprint('admin', __name__)

@bp.route('/admin')
@admin_required # só admin
def admin():
    users = get_all_users()
    return render_template('admin.html', users=users)

@bp.route('/admin/create', methods=['GET','POST'])
@admin_required
def create():
    create_user(
        request.form.get('nome'),
        request.form.get('email'),
        generate_password_hash(request.form.get('senha'))
    )
    return redirect(url_for('admin.admin'))

@bp.route('/admin/edit/<int:id>', methods=['GET', 'POST'])
@admin_required
def edit(id):
    user = get_user_by_id(id)

    if request.method == 'POST':
        update_user(
            id,
            request.form.get('nome'),
            request.form.get('email')
        )
        return redirect(url_for('admin.admin'))
    return render_template('edit_user.html', user=user)

@bp.route('/admin/delete/<int:id>')
@admin_required
def delete(id):
    delete_user(id)
    return redirect(url_for('admin.admin'))