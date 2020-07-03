from tkinter import *
from tkinter import messagebox
import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS professores (nome TEXT NOT NULL, cpf TEXT NOT NULL, departamento TEXT NOT NULL)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (nome TEXT NOT NULL, cpf TEXT NOT NULL)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS disciplinas (nome TEXT NOT NULL, codigo TEXT NOT NULL)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS relatorioprof (cpf TEXT NOT NULL, turma TEXT, disciplina TEXT, per TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS relatorioaluno (cpf TEXT NOT NULL, turma TEXT, disciplina TEXT, per TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS turmas (cod TEXT NOT NULL, per TEXT NOT NULL, codd TEXT NOT NULL, cpfp TEXT, cpfa TEXT)''')
conn.close()
lista_a = []
lista_p = []


#-------------------------------------------Funçoes professor funcionalidades-------------------------------------------#

# Funçoes professor menus
def professor():
    frame_prof.place(x=0, y=0)
    frame_principal.place(x=10000, y=0)
def cadastro_prof():
    frame_prof.place(x=10000, y=0)
    frame_cad_prof.place(x=0, y=0)
    ent_cad_nome_prof.focus()
def consulta_prof():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM professores''')
    var = cursor.fetchall()
    lista_cons_prof.insert(0,'_'*14 + '| Professores Cadastrados |' + '_'*25)
    for i in var:
        lista_cons_prof.insert(1," "*15 + '   |   '.join(i))
    ent_cons_cpf_prof.focus()
    frame_cons_prof.place(x=0, y=0)
    frame_prof.place(x=10000, y=0)
def atualizar_prof():
    frame_prof.place(x=10000, y=0)
    frame_att_prof.place(x=0, y=0)
    ent_att_cpf_antigo_prof.focus()
def remover_prof():
    ent_rem_prof.focus()
    frame_prof.place(x=10000, y=0)
    frame_rem_prof.place(x=0, y=0)
def relatorio_prof():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpf FROM relatorioprof''')
    lista_rel_prof.insert(0, '_'*15 + '| Relatórios Disponíveis |' + '_'*15)
    for i in cursor.fetchall():
        cursor.execute('''SELECT * FROM professores WHERE cpf = ?''',(i))
        var = cursor.fetchone()
        if (' '*15 + '|  ' + ('    |    '.join(var)) + '  |') not in lista_rel_prof.get(0,END):
            lista_rel_prof.insert(1,' '*15 + '|  ' + ('    |    '.join(var)) + '  |')
        else:
            pass
    conn.close()
    frame_rel_prof.place(x=0,y=0)
    frame_prof.place(x=10000,y=0)
#Funçoes professor botoes
def vlt_prof_menu():
    frame_prof.place(x=10000, y=0)
    frame_principal.place(x=0, y=0)
def vlt_rem_prof():
    frame_prof.place(x=0, y=0)
    frame_rem_prof.place(x=10000, y=0)
def vlt_cad_prof():
    frame_prof.place(x=0, y=0)
    frame_cad_prof.place(x=10000, y=0)
    ent_cad_cpf_prof.delete(0, END)
    ent_cad_nome_prof.delete(0, END)
    ent_cad_dep_prof.delete(0, END)
def vlt_cons_prof():
    txt_cons_prof1['text'] = ''
    txt_cons_prof2['text'] = ''
    ent_cons_cpf_prof.delete(0,END)
    lista_cons_prof.delete(0, END)
    frame_prof.place(x=0, y=0)
    frame_cons_prof.place(x=10000, y=0)
def vlt_att_prof():
    frame_prof.place(x=0, y=0)
    frame_att_prof.place(x=10000, y=0)
    ver_att_prof['text'] = ''
    ent_att_cpf_antigo_prof.delete(0, END)
    ent_att_dep_novo_prof.delete(0, END)
    ent_att_cpf_novo_prof.delete(0, END)
    ent_att_nome_novo_prof.delete(0, END)
    ent_att_cpf_novo_prof['state'] = 'disabled'
    ent_att_dep_novo_prof['state'] = 'disabled'
    ent_att_nome_novo_prof['state'] = 'disabled'
def vlt_rel_prof():
    ent_rel_prof_per.delete(0,END)
    ent_rel_prof_cpf.delete(0,END)
    lista_rel_prof.delete(0,END)
    frame_prof.place(x=0,y=0)
    frame_rel_prof.place(x=10000,y=0)
def ver_att_prof():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpf FROM professores WHERE cpf = ?''', (ent_att_cpf_antigo_prof.get(),))
    if cursor.fetchone() is None:
        ver_att_prof['fg'] = 'red'
        ver_att_prof['text'] = '✘'
        ent_att_cpf_novo_prof.delete(0, END)
        ent_att_dep_novo_prof.delete(0, END)
        ent_att_nome_novo_prof.delete(0, END)
        ent_att_cpf_novo_prof['state'] = 'disabled'
        ent_att_dep_novo_prof['state'] = 'disabled'
        ent_att_nome_novo_prof['state'] = 'disabled'
    else:
        ent_att_cpf_novo_prof.delete(0,END)
        ent_att_dep_novo_prof.delete(0,END)
        ent_att_nome_novo_prof.delete(0,END)
        ver_att_prof['fg'] = 'limegreen'
        ver_att_prof['text'] = '✓'
        ent_att_cpf_novo_prof['state'] = 'normal'
        ent_att_dep_novo_prof['state'] = 'normal'
        ent_att_nome_novo_prof['state'] = 'normal'
        cursor.execute('''SELECT * FROM professores WHERE cpf = ?''', (ent_att_cpf_antigo_prof.get(),))
        var = cursor.fetchone()
        ent_att_cpf_novo_prof.insert(0,var[1])
        ent_att_dep_novo_prof.insert(0,var[2])
        ent_att_nome_novo_prof.insert(0,var[0])
    conn.close()
def ver_att_prof1():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpf FROM professores WHERE cpf = ?''', (ent_att_cpf_antigo_prof.get(),))
    if cursor.fetchone() is None:
        return False

    else:
        return True
def ver_cad_turm_prof1():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpf FROM professores WHERE cpf = ?''', (cpf_prof_turm.get(),))
    if cursor.fetchone() is None:
        return False

    else:
        return True
def verifica_cpf_cad_prof():
    x = 0
    if len(ent_cad_cpf_prof.get()) == 11:
        for i in ent_cad_cpf_prof.get():
            if i.isalpha():
                x += 1
            else:
                continue
        if x > 0:
            return False
        else:
            return True
    else:
        return False
def verifica_cpf_cad_turm_prof():
    x = 0
    if len(cpf_prof_turm.get()) == 11:
        for i in cpf_prof_turm.get():
            if i.isalpha():
                x += 1
            else:
                continue
        if x > 0:
            return False
        else:
            return True
    else:
        return False
def verifica_cpf_att_prof():
    x = 0
    if len(ent_att_cpf_novo_prof.get()) == 11:
        for i in ent_att_cpf_novo_prof.get():
            if i.isalpha():
                x += 1
            else:
                continue
        if x > 0:
            return False
        else:
            return True
    else:
        return False
def verifica_nome_cad_prof():
    x = 0
    for i in ent_cad_nome_prof.get():
        if i.isnumeric():
            x += 1
        else:
            continue
    if x > 0:
        return False
    else:
        return True
def valida_cpf_prof():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpf FROM professores WHERE cpf = ?''', (ent_cad_cpf_prof.get(),))
    return cursor.fetchone()
def ver_rem_prof1():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpf FROM professores WHERE cpf = ?''', (ent_rem_prof.get(),))
    if cursor.fetchone() is None:
        return False

    else:
        return True
def rem_prof():
    if ver_rem_prof1() == False:
        messagebox.showerror('Remoção', 'CPF não encontrado no sistema!')
    else:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM professores WHERE cpf = ?''',
                       (ent_rem_prof.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo('Remoção','Informações deletadas com sucesso!')
        ent_rem_prof.delete(0,END)
def att_prof():
    if ver_att_prof1() == False:
        messagebox.showerror('Atualização', 'Insira um CPF disponível no sistema!')
    elif verifica_cpf_att_prof() == True:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''UPDATE professores SET nome = ?, cpf = ?, departamento = ? WHERE cpf = ?''',
                       (ent_att_nome_novo_prof.get(), ent_att_cpf_novo_prof.get(), ent_att_dep_novo_prof.get(),
                        ent_att_cpf_antigo_prof.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo('Atualização', 'Informações atualizadas com êxito!')
        ent_att_cpf_antigo_prof.delete(0, END)
        ent_att_dep_novo_prof.delete(0, END)
        ent_att_cpf_novo_prof.delete(0, END)
        ent_att_nome_novo_prof.delete(0, END)
        ent_att_cpf_novo_prof['state'] = 'disabled'
        ent_att_dep_novo_prof['state'] = 'disabled'
        ent_att_nome_novo_prof['state'] = 'disabled'
    else:
        messagebox.showerror('Atualização', 'Insira um CPF válido!')
def cons_prof():
    lista_cons_prof.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM professores WHERE cpf = ?''', (ent_cons_cpf_prof.get(),))
    var = cursor.fetchone()
    if var is None:
        txt_cons_prof1['text'] = 'CPF não encontrado!'
        txt_cons_prof2['text'] = '⚠'
    else:
        txt_cons_prof1['text'] = ''
        txt_cons_prof2['text'] = ''
        lista_cons_prof.insert(0, ">|----------| Nome |---------------| CPF |--------| Departamento |-------|<")
        lista_cons_prof.insert(1, '>|'+'-'*91+'|<')
        lista_cons_prof.insert(2, '>|---|  ' + "   |   ".join(var) + '  |----------|<')
    conn.close()
    ent_cons_cpf_prof.delete(0, END)
def cad_prof():
    if verifica_cpf_cad_prof() == False:
        messagebox.showerror('Cadastro', 'CPF Inválido')
    elif verifica_nome_cad_prof() == False:
        messagebox.showerror('Cadastro', 'Nome Inválido')
    elif valida_cpf_prof() is None:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO professores (nome, cpf, departamento)
        VALUES (?,?,?)''', (ent_cad_nome_prof.get(), ent_cad_cpf_prof.get(), ent_cad_dep_prof.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo('Cadastro', 'Professor cadastrado com sucesso!')
        ent_cad_cpf_prof.delete(0, END)
        ent_cad_nome_prof.delete(0, END)
        ent_cad_dep_prof.delete(0, END)
    else:
        messagebox.showerror('Cadastro', 'CPF já cadastrado')
def rel_prof():
    lista_rel_prof.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM relatorioprof WHERE (cpf = ?)''',(ent_rel_prof_cpf.get(),))
    var = cursor.fetchall()
    if ent_rel_prof_per.get() == '':
        lista_rel_prof.insert(1, '>----- Turma ------ Periodo----<')
        lista_rel_prof.insert(2, ' ' + '-' * 85)
    else:
        lista_rel_prof.insert(1, '>---------- CPF ------------ Turma ------ Disc -------- Periodo----<')
        lista_rel_prof.insert(2, ' ' + '-' * 85)
    for tpl in var:
        if ent_rel_prof_per.get() == '':
            lista_rel_prof.insert(3, '>-- ' + tpl[1] +"    |    " + tpl[3] + ' ---<')
        else:
            if ent_rel_prof_per.get() in tpl:

                lista_rel_prof.insert(3, '>-- ' + "    |    ".join(tpl) + ' ---<')

#Funçoes alunos menus
def relatorio_alun():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpf FROM relatorioaluno''')
    lista_rel_alun.insert(0, '_' * 15 + '| Relatórios Disponíveis |' + '_' * 15)
    for i in cursor.fetchall():
        cursor.execute('''SELECT * FROM alunos WHERE cpf = ?''', (i))
        var = cursor.fetchone()
        if (' ' * 25 + '|  ' + ('    |    '.join(var)) + '  |') not in lista_rel_alun.get(0,END):
            lista_rel_alun.insert(1, ' ' * 25 + '|  ' + ('    |    '.join(var)) + '  |')
        else:
           pass
    conn.close()
    frame_rel_alun.place(x=0,y=0)
    frame_alun.place(x=10000,y=0)
def aluno():
    frame_alun.place(x=0, y=0)
    frame_principal.place(x=10000, y=0)
def cadastro_aluno():
    ent_cad_nome_alun.focus()
    frame_cad_alun.place(x=0, y=0)
    frame_alun.place(x=10000, y=0)
def consulta_aluno():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM alunos''')
    var = cursor.fetchall()
    lista_cons_alun.insert(0, '_' * 16 + '| Alunos Cadastrados |' + '_' * 25)
    for i in var:
        lista_cons_alun.insert(1, " " * 25 + '   |   '.join(i))
    ent_cons_cpf_alun.focus()
    frame_cons_alun.place(x=0, y=0)
    frame_alun.place(x=10000, y=0)
def remover_aluno():
    ent_rem_alun.focus()
    frame_rem_alun.place(x=0, y=0)
    frame_alun.place(x=10000, y=0)
def atualizar_aluno():
    ent_att_cpf_antigo_alun.focus()
    frame_att_alun.place(x=0, y=0)
    frame_alun.place(x=10000, y=0)
#Funçoes alunos botoes
def vlt_cons_alun():
    txt_cons_alun1['text'] = ''
    ent_cons_cpf_alun.delete(0,END)
    lista_cons_alun.delete(0, END)
    frame_cons_alun.place(x=10000, y=0)
    frame_alun.place(x=0, y=0)
def vlt_alun_menu():
    frame_alun.place(x=10000, y=0)
    frame_principal.place(x=0, y=0)
def vlt_cad_alun():
    frame_alun.place(x=0, y=0)
    frame_cad_alun.place(x=10000, y=0)
def vlt_rem_alun():
    frame_rem_alun.place(x=10000, y=0)
    frame_alun.place(x=0, y=0)
def vlt_att_alun():
    ent_att_cpf_antigo_alun.delete(0, END)
    ent_att_cpf_novo_alun.delete(0, END)
    ent_att_nome_novo_alun.delete(0, END)
    ver_att_alun['text'] = ''
    ent_att_cpf_novo_alun['state'] = 'disabled'
    ent_att_nome_novo_alun['state'] = 'disabled'
    frame_att_alun.place(x=10000, y=0)
    frame_alun.place(x=0, y=0)
def ver_att_alun():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpf FROM alunos WHERE cpf = ?''', (ent_att_cpf_antigo_alun.get(),))
    if cursor.fetchone() is None:
        ver_att_alun['fg'] = 'red'
        ver_att_alun['text'] = '✘'
        ent_att_cpf_novo_alun.delete(0, END)
        ent_att_nome_novo_alun.delete(0, END)
        ent_att_cpf_novo_alun['state'] = 'disabled'
        ent_att_nome_novo_alun['state'] = 'disabled'
    else:
        ent_att_cpf_novo_alun.delete(0,END)
        ent_att_nome_novo_alun.delete(0,END)
        ver_att_alun['fg'] = 'limegreen'
        ver_att_alun['text'] = '✓'
        ent_att_cpf_novo_alun['state'] = 'normal'
        ent_att_nome_novo_alun['state'] = 'normal'
        cursor.execute('''SELECT * FROM alunos WHERE cpf = ?''', (ent_att_cpf_antigo_alun.get(),))
        var = cursor.fetchone()
        ent_att_cpf_novo_alun.insert(0, var[1])
        ent_att_nome_novo_alun.insert(0, var[0])
    conn.close()
def ver_att_alun1():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpf FROM alunos WHERE cpf = ?''', (ent_att_cpf_antigo_alun.get(),))
    if cursor.fetchone() is None:
        return False
    else:
        return True
def verifica_cpf_cad_turm_aluno():
    x = 0
    if len(cpf_alun_turm.get()) == 11:
        for i in cpf_alun_turm.get():
            if i.isalpha():
                x += 1
            else:
                continue
        if x > 0:
            return False
        else:
            return True
    else:
        return False
def ver_cad_turm_alun1():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpf FROM alunos WHERE cpf = ?''', (cpf_alun_turm.get(),))
    if cursor.fetchone() is None:
        return False
    else:
        return True
def vlt_rel_alun():
    ent_rel_alun_cpf.delete(0,END)
    ent_rel_alun_per.delete(0,END)
    lista_rel_alun.delete(0,END)
    frame_rel_alun.place(x=10000,y=0)
    frame_alun.place(x=0,y=0)
def valida_cpf_aluno():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpf FROM alunos WHERE cpf = ?''', (ent_cad_cpf_alun.get(),))
    return cursor.fetchone()
def verifica_cpf_cad_aluno():
    x = 0
    if len(ent_cad_cpf_alun.get()) == 11:
        for i in ent_cad_cpf_prof.get():
            if i.isalpha():
                x += 1
            else:
                continue
        if x > 0:
            return False
        else:
            return True
    else:
        return False
def verifica_cpf_att_aluno():
    x = 0
    if len(ent_att_cpf_novo_alun.get()) == 11:
        for i in ent_att_cpf_novo_alun.get():
            if i.isalpha():
                x += 1
            else:
                continue
        if x > 0:
            return False
        else:
            return True
    else:
        return False
def verifica_nome_cad_aluno():
    x = 0
    for i in ent_cad_nome_alun.get():
        if i.isnumeric():
            x += 1
        else:
            continue
    if x > 0:
        return False
    else:
        return True
def ver_rem_alun1():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpf FROM alunos WHERE cpf = ?''', (ent_rem_alun.get(),))
    if cursor.fetchone() is None:
        return False

    else:
        return True
def rem_alun():
    if ver_rem_alun1() == False:
        messagebox.showerror('Remoção', 'CPF não encontrado no sistema!')
    else:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM alunos WHERE cpf = ?''',
                       (ent_rem_alun.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo('Remoção','Informações deletadas com sucesso!')
        ent_rem_alun.delete(0,END)
def cons_alun():
    lista_cons_alun.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM alunos WHERE cpf = ?''', (ent_cons_cpf_alun.get(),))
    var = cursor.fetchone()
    if var is None:
        txt_cons_alun1['text'] = 'CPF não encontrado!'
        txt_cons_alun2['text'] = '⚠'
    else:
        txt_cons_alun1['text'] = ''
        txt_cons_alun2['text'] = ''
        lista_cons_alun.insert(0, ">|----------| Nome |---------------| CPF |-------------------|<")
        lista_cons_alun.insert(1, '>|' + '-' * 68 + '|<')
        lista_cons_alun.insert(2, '>|---|  ' + "   |   ".join(var) + '  |----------|<')
    conn.close()
    ent_cons_cpf_alun.delete(0, END)
def cad_aluno():
    if verifica_nome_cad_aluno() == False:
        messagebox.showerror('Cadastro', 'Nome inválido!')
    elif verifica_cpf_cad_aluno() == False:
        messagebox.showerror('Cadastro', 'CPF inválido!')
    elif valida_cpf_aluno() is None:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO alunos (nome, cpf)
            VALUES (?,?)''', (ent_cad_nome_alun.get(), ent_cad_cpf_alun.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo('Cadastro', 'Aluno cadastrado com sucesso! ')
        ent_cad_nome_alun.delete(0, END)
        ent_cad_cpf_alun.delete(0, END)
    else:
        messagebox.showerror('Cadastro', 'CPF já cadastrado!')
def att_alun():
    if ver_att_alun1() == False:
        messagebox.showerror('Atualização', 'Insira um CPF disponível no sistema!')
    elif verifica_cpf_att_aluno() == True:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''UPDATE alunos SET nome = ?, cpf = ? WHERE cpf = ?''',
                       (ent_att_nome_novo_alun.get(), ent_att_cpf_novo_alun.get(), ent_att_cpf_antigo_alun.get(),))
        conn.commit()
        messagebox.showinfo('Atualização', 'Informações atualizadas com êxito!')
        ent_att_cpf_antigo_alun.delete(0, END)
        ent_att_cpf_novo_alun.delete(0, END)
        ent_att_nome_novo_alun.delete(0, END)
        ent_att_cpf_novo_alun['state'] = 'disabled'
        ent_att_nome_novo_alun['state'] = 'disabled'
    else:
        messagebox.showerror('Atualização', 'Insira um CPF válido!')
def rel_alun():
    lista_rel_alun.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM relatorioaluno WHERE (cpf = ?)''',(ent_rel_alun_cpf.get(),))
    var = cursor.fetchall()
    if ent_rel_alun_per.get() == '':
        lista_rel_alun.insert(1, '>----- Turma ------ Periodo----<')
        lista_rel_alun.insert(2, ' ' + '-' * 85)
    else:
        lista_rel_alun.insert(1, '>---------- CPF ------------ Turma ------ Disc -------- Periodo----<')
        lista_rel_alun.insert(2, ' ' + '-' * 85)
    for tpl in var:
        if ent_rel_alun_per.get() == '':
            lista_rel_alun.insert(3, '>-- ' + tpl[1] +"    |    " + tpl[3] + ' ---<')
        else:
            if  ent_rel_alun_per.get() in tpl:
                lista_rel_alun.insert(3, '>-- ' + "    |    ".join(tpl) + ' ---<')


#Funçoes disciplinas menu
def disciplina():
    frame_disc.place(x=0, y=0)
    frame_principal.place(x=10000, y=0)
def cadastro_disc():
    ent_cad_nome_disc.focus()
    frame_cad_disc.place(x=0, y=0)
    frame_principal.place(x=10000, y=0)
def consulta_disc():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM disciplinas''')
    var = cursor.fetchall()
    lista_cons_disc.insert(0, '_' * 14 + '| Disciplinas Disponíveis |' + '_' * 25)
    for i in var:
        lista_cons_disc.insert(1, " " * 20 + '   |   '.join(i))
    ent_cons_cod_disc.focus()
    frame_cons_disc.place(x=0, y=0)
    frame_disc.place(x=10000, y=0)
def atualizar_disc():
    ent_att_cod_antigo_disc.focus()
    frame_att_disc.place(x=0, y=0)
    frame_disc.place(x=10000, y=0)
def remover_disc():
    ent_rem_disc.focus()
    frame_rem_disc.place(x=0, y=0)
    frame_disc.place(x=10000, y=0)

#Funçoes disciplinas botoes
def vlt_cad_disc():
    frame_cad_disc.place(x=10000, y=0)
    frame_principal.place(x=0, y=0)
def vlt_disc_menu():
    frame_disc.place(x=10000, y=0)
    frame_principal.place(x=0, y=0)
def vlt_cons_disc():
    txt_cons_disc1['text'] = ''
    txt_cons_disc2['text'] = ''
    ent_cons_cod_disc.delete(0,END)
    lista_cons_disc.delete(0, END)
    frame_cons_disc.place(x=10000, y=0)
    frame_disc.place(x=0, y=0)
def vlt_att_disc():
    ent_att_cod_antigo_disc.delete(0, END)
    ent_att_cod_novo_disc.delete(0, END)
    ent_att_nome_novo_disc.delete(0, END)
    ent_att_nome_novo_disc['state'] = 'disabled'
    ent_att_cod_novo_disc['state'] = 'disabled'
    frame_att_disc.place(x=10000, y=0)
    frame_disc.place(x=0, y=0)
def vlt_rem_disc():
    frame_rem_disc.place(x=10000, y=0)
    frame_disc.place(x=0, y=0)
def ver_cad_turm_disc1():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT codigo FROM disciplinas WHERE codigo = ?''', (ent_cad_cod_disc_turm.get(),))
    if cursor.fetchone() is None:
        return False
    else:
        return True
def ver_att_disc():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT codigo FROM disciplinas WHERE codigo = ?''', (ent_att_cod_antigo_disc.get(),))
    if cursor.fetchone() is None:
        ent_att_nome_novo_disc.delete(0, END)
        ent_att_cod_novo_disc.delete(0, END)
        ver_att_disc['fg'] = 'red'
        ver_att_disc['text'] = '✘'
        ent_att_nome_novo_disc['state'] = 'disabled'
        ent_att_cod_novo_disc['state'] = 'disabled'
    else:
        ent_att_nome_novo_disc.delete(0,END)
        ent_att_cod_novo_disc.delete(0,END)
        ver_att_disc['fg'] = 'limegreen'
        ver_att_disc['text'] = '✓'
        ent_att_nome_novo_disc['state'] = 'normal'
        ent_att_cod_novo_disc['state'] = 'normal'
        cursor.execute('''SELECT * FROM disciplinas WHERE codigo = ?''', (ent_att_cod_antigo_disc.get(),))
        var = cursor.fetchone()
        ent_att_nome_novo_disc.insert(0,var[0])
        ent_att_cod_novo_disc.insert(0,var[1])
    conn.close()
def ver_att_disc1():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT codigo FROM disciplinas WHERE codigo = ?''', (ent_att_cod_antigo_disc.get(),))
    if cursor.fetchone() is None:
        return False
    else:
        return True
def valida_disciplina():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT codigo FROM disciplinas WHERE codigo = ?''', (ent_cad_cod_disc.get(),))
    return cursor.fetchone()
def ver_rem_disc1():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT codigo FROM disciplinas WHERE codigo = ?''', (ent_rem_disc.get(),))
    if cursor.fetchone() is None:
        return False
    else:
        return True
def rem_disc():
    if ver_rem_disc1() == False:
        messagebox.showerror('Remoção', 'Código não encontrado no sistema!')
        ent_rem_disc.delete(0, END)
    else:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM disciplinas WHERE codigo = ?''',
                       (ent_rem_disc.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo('Remoção','Informações deletadas com sucesso!')

        ent_rem_disc.delete(0,END)
def cad_disc():
    if valida_disciplina() is None:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO disciplinas (nome,codigo) VALUES (?,?)''',
                       (ent_cad_nome_disc.get(), ent_cad_cod_disc.get(),))
        conn.commit()
        conn.close()
        ent_cad_cod_disc.delete(0, END)
        ent_cad_nome_disc.delete(0, END)
        messagebox.showinfo('Cadastro', 'Disciplina cadastrada com sucesso!')
    else:
        messagebox.showerror('Cadastro', 'Código já cadastrado!')
def att_disc():
    if ver_att_disc1() == False:
        messagebox.showerror('Atualização', 'Insira um código disponível no sistema!')
    else:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''UPDATE disciplinas SET nome = ?, codigo = ? WHERE codigo = ?''',
                       (ent_att_nome_novo_disc.get(), ent_att_cod_novo_disc.get(), ent_att_cod_antigo_disc.get(),))
        conn.commit()
        messagebox.showinfo('Atualização', 'Informações atualizadas com êxito!')
        ent_att_cod_antigo_disc.delete(0, END)
        ent_att_cod_novo_disc.delete(0, END)
        ent_att_nome_novo_disc.delete(0, END)
        ent_att_nome_novo_disc['state'] = 'disabled'
        ent_att_cod_novo_disc['state'] = 'disabled'
def cons_disc():
    lista_cons_disc.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM disciplinas WHERE codigo = ?''', (ent_cons_cod_disc.get(),))
    var = cursor.fetchone()
    if var is None:
        txt_cons_disc1['text'] = 'Código não encontrado!'
        txt_cons_disc2['text'] = '⚠'
    else:
        txt_cons_disc1['text'] = ''
        txt_cons_disc2['text'] = ''
        lista_cons_disc.insert(0, ">|----------| Nome |---------------| Código |-------------------|<")
        lista_cons_disc.insert(1, '>|' + '-' * 68 + '|<')
        lista_cons_disc.insert(2, '>|---|  ' + "   |   ".join(var) + '  |----------|<')

    conn.close()
    ent_cons_cod_disc.delete(0, END)

# Função turmas menus
def turma():
    frame_turm.place(x=0, y=0)
    frame_principal.place(x=10000, y=0)
def cadastro_turma():

    ent_cad_cod_turm.focus()
    frame_cad_turm.place(x=0, y=0)
    frame_turm.place(x=10000, y=0)
def atualizar_turma():
    frame_att_turm.place(x=0, y=0)
    frame_turm.place(x=10000, y=0)
def remover_turma():
    frame_rem_turm.place(x=0, y=0)
    frame_turm.place(x=10000, y=0)
def consulta_turma():
    lista_cons_turm.delete(0, END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cod FROM turmas''')
    var = cursor.fetchall()
    lista_cons_turm.insert(0,'_'*23 + '| Turmas Cadastradas |' + '_'*30)
    for i in var:
        lista_cons_turm.insert(1,'_'*30+ '| '+ ''.join(i) + ' |' + '_'*31)
    ent_cons_cod_turm.focus()
    frame_cons_turm.place(x=0, y=0)
    frame_turm.place(x=10000, y=0)
def ata_turma():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cod FROM turmas''')
    lista_ata_turm.insert(0, '_' * 25 + '| Atas Disponíveis |' + '_' * 25)
    for i in cursor.fetchall():
        cursor.execute('''SELECT cod FROM turmas WHERE cod = ?''', (i))
        var = cursor.fetchone()
        if (' ' * 15 + '|  ' + ('    |    '.join(var)) + '  |') not in lista_ata_turm.get(0, END):
            lista_ata_turm.insert(1, '_' * 27 + '|  ' + 'Turma: ' + (''.join(var)) + '  |' + '_' * 27)
        else:
            pass
    conn.close()
    frame_ata_turm.place(x=0,y=0)
    frame_turm.place(x=10000,y=0)
def insert_cpf():
    frame_cad_turm_insert.place(x=0,y=0)
    frame_cad_turm.place(x=10000,y=0)

# Funções botões turmas
def slt_cpf_prof():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpfp FROM turmas WHERE cod = ?''', (ent_att_cod_novo_turm.get(),))
    var = cursor.fetchone()[0]
    lista_p = var.split('-')
    var = lista_att_turm_prof.get(lista_att_turm_prof.curselection()[0])
    a = ''
    for i in var:
        if i.isnumeric():
            a += i
    cpf_prof_att_turm.insert(0,a)
    conn.close()
def ver_cpf_att_turm_prof():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpf FROM professores WHERE cpf = ?''',(cpf_prof_att_turm.get(),))
    if cursor.fetchone() is None:
        return False
    else:
        return True
def att_cpf_prof():
    if ver_cpf_att_turm_prof() is False:
        messagebox.showerror('Atualização de Turma', 'Insira um CPF disponível no sistema!')
    else:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT cpfp FROM turmas WHERE cod = ?''', (ent_att_cod_novo_turm.get(),))
        var = cursor.fetchone()[0]
        lista_p = var.split('-')
        var = lista_att_turm_prof.get(lista_att_turm_prof.curselection())
        a = ''
        for i in var:
            if i.isnumeric():
                a += i
        pos = lista_p.index(a)
        lista_p.pop(pos)
        lista_p.insert(pos, cpf_prof_att_turm.get())
        cursor.execute('''UPDATE turmas SET cpfp = ? WHERE cod = ?''',
                       (('-'.join(lista_p)), ent_att_cod_novo_turm.get()))
        conn.commit()
        conn.close()
        lista_att_turm_prof.delete(0, END)
        for i in lista_p:
            lista_att_turm_prof.insert(0, '_' * 9 + '|' + i + '|' + '_' * 9)
        cpf_prof_att_turm.delete(0,END)
def slt_cpf_aluno():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpfa FROM turmas WHERE cod = ?''', (ent_att_cod_novo_turm.get(),))
    var = cursor.fetchone()[0]
    lista_a = var.split('-')
    var = lista_att_turm_alun.get(lista_att_turm_alun.curselection()[0])
    a = ''
    for i in var:
        if i.isnumeric():
            a += i
    cpf_alun_att_turm.insert(0,a)
    conn.close()
def ver_cpf_att_turm_aluno():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpf FROM alunos WHERE cpf = ?''',(cpf_alun_att_turm.get(),))
    if cursor.fetchone() is None:
        return False
    else:
        return True
def att_cpf_aluno():
    if ver_cpf_att_turm_aluno() is False:
        messagebox.showerror('Atualização de CPF', 'Insira um CPF disponível no sistema!')
    else:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT cpfa FROM turmas WHERE cod = ?''', (ent_att_cod_novo_turm.get(),))
        var = cursor.fetchone()[0]
        lista_a = var.split('-')
        var = lista_att_turm_alun.get(lista_att_turm_alun.curselection())
        a = ''
        for i in var:
            if i.isnumeric():
                a += i
        pos = lista_a.index(a)
        lista_a.pop(pos)
        lista_a.insert(pos, cpf_alun_att_turm.get())
        cursor.execute('''UPDATE turmas SET cpfa = ? WHERE cod = ?''',
                       (('-'.join(lista_a)), ent_att_cod_novo_turm.get()))
        conn.commit()
        conn.close()
        lista_att_turm_alun.delete(0, END)
        for i in lista_a:
            lista_att_turm_alun.insert(0, '_' * 9 + '|' + i + '|' + '_' * 9)
        cpf_alun_att_turm.delete(0,END)
def ver_att_turma():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM turmas WHERE cod = ?''',(ent_att_cod_turm.get(),))
    var = cursor.fetchone()
    if var is None:
        check_att_turm['text'] = '✘'
        check_att_turm['fg'] = 'red'
        ent_att_cod_novo_turm.delete(0, END)
        ent_att_per_turm.delete(0, END)
        ent_att_cod_disc_turm.delete(0, END)
        ent_att_cod_disc_turm['state'] = 'disabled'
        ent_att_per_turm['state'] = 'disabled'
        ent_att_cod_novo_turm['state'] = 'disabled'
    else:
        ent_att_cod_novo_turm.delete(0,END)
        ent_att_per_turm.delete(0,END)
        ent_att_cod_disc_turm.delete(0,END)
        check_att_turm['text'] = '✓'
        check_att_turm['fg'] = 'limegreen'
        ent_att_cod_disc_turm['state'] = 'normal'
        ent_att_per_turm['state'] = 'normal'
        ent_att_cod_novo_turm['state'] = 'normal'
        ent_att_cod_novo_turm.insert(0,var[0])
        ent_att_per_turm.insert(0,var[2])
        ent_att_cod_disc_turm.insert(0,var[1])
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT cpfa FROM turmas WHERE cod = ?''', (ent_att_cod_turm.get(),))
        var = cursor.fetchone()[0]
        lista_a = var.split('-')
        lista_att_turm_alun.delete(0, END)
        for i in lista_a:
            lista_att_turm_alun.insert(0, '_'*9 + '|' + i + '|' + '_'*9)
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT cpfp FROM turmas WHERE cod = ?''', (ent_att_cod_turm.get(),))
        var = cursor.fetchone()[0]
        lista_p = var.split('-')
        lista_att_turm_prof.delete(0, END)
        for i in lista_p:
            lista_att_turm_prof.insert(0, '_' * 9 + '|' + i + '|' + '_' * 9)
    conn.close()
def verifica_turma():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM turmas WHERE cod = ?''',(ent_cad_cod_turm.get(),))
    if cursor.fetchone() is None:
        return False
    else:
        return True
def cons_turm():
    try:
        lista_cons_turm.delete(0, END)
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT cod,per,codd FROM turmas WHERE cod = ?''',(ent_cons_cod_turm.get(),))
        lista_cons_turm.insert(0, '      Turma            |              Período                 |             Cod disciplina')
        lista_cons_turm.insert(1, '-'*150)
        lista_cons_turm.insert(2, '         ' + "              |                   ".join(cursor.fetchone()))
        lista_cons_turm.insert(3, '-'*150)
        lista_cons_turm.insert(4, 'Professores:')
        cursor.execute('''SELECT cpfp FROM turmas WHERE cod = ?''',(ent_cons_cod_turm.get(),))
        conn1 = sqlite3.connect('database.db')
        cursor1 = conn1.cursor()
        for i in cursor.fetchone():
            for c in i.split('-'):
                cursor1.execute('''SELECT nome,cpf FROM professores WHERE cpf = ?''', (c,))
                lista_cons_turm.insert(5, 'Nome:  ' + " | CPF:  ".join(cursor1.fetchone()))
        lista_cons_turm.insert(6, '-'*150)
        lista_cons_turm.insert(7, 'Alunos: ')
        cursor.execute('''SELECT cpfa FROM turmas WHERE cod = ?''',(ent_cons_cod_turm.get(),))
        conn2 = sqlite3.connect('database.db')
        cursor2 = conn2.cursor()
        for i in cursor.fetchone():
            for c in i.split('-'):
                cursor2.execute('''SELECT nome,cpf FROM alunos WHERE cpf = ?''', (c,))
                lista_cons_turm.insert(8, 'Nome:  ' + " | CPF:  ".join(cursor2.fetchone()))
        conn.close()
        conn1.close()
        conn2.close()
        txt_cons_turm1['text'] = ''
        txt_cons_turm2['text'] = ''
    except TypeError:
        txt_cons_turm1['text'] = 'Turma não encontrada!'
        txt_cons_turm2['text'] = '⚠'
def ata_turm():
    try:
        lista_ata_turm.delete(0, END)
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT cod,per,codd FROM turmas WHERE cod = ?''',(ent_ata_turm_cod.get(),))
        lista_ata_turm.insert(0,'|' + '_'*26 + '| Ata de Turma |'+ '_'*25 + '|')
        lista_ata_turm.insert(1, '      Turma            |              Período                 |             Cod disciplina')
        lista_ata_turm.insert(2, '-'*150)
        lista_ata_turm.insert(3, '         ' + "              |                   ".join(cursor.fetchone()))
        lista_ata_turm.insert(4, '-'*150)
        lista_ata_turm.insert(5, ' ' * 75 + '|               Assinatura                    |')
        lista_ata_turm.insert(6, '-' * 150)
        lista_ata_turm.insert(7, 'Professores:')
        cursor.execute('''SELECT cpfp FROM turmas WHERE cod = ?''',(ent_ata_turm_cod.get(),))
        conn1 = sqlite3.connect('database.db')
        cursor1 = conn1.cursor()
        for i in cursor.fetchone():
            for c in i.split('-'):
                cursor1.execute('''SELECT nome,cpf FROM professores WHERE cpf = ?''', (c,))
                lista_ata_turm.insert(8, 'Nome:  ' + " | CPF:  ".join(cursor1.fetchone()) + ' | ' + 'x'  +'_'*25)
        lista_ata_turm.insert(9, '-'*150)
        lista_ata_turm.insert(10, 'Alunos: ')
        cursor.execute('''SELECT cpfa FROM turmas WHERE cod = ?''',(ent_ata_turm_cod.get(),))
        conn2 = sqlite3.connect('database.db')
        cursor2 = conn2.cursor()
        for i in cursor.fetchone():
            for c in i.split('-'):
                cursor2.execute('''SELECT nome,cpf FROM alunos WHERE cpf = ?''', (c,))
                lista_ata_turm.insert(11, 'Nome:  ' + " | CPF:  ".join(cursor2.fetchone())+ ' | ' + 'x'  +'_'*25)
        conn.close()
        conn1.close()
        conn2.close()
        txt_ata_turm1['text'] = ''
        txt_ata_turm2['text'] = ''
    except TypeError:
        txt_ata_turm1['text'] = 'Turma não encontrada!'
        txt_ata_turm2['text'] = '⚠'
def cad_turma():
    if ver_cad_turm_disc1() is False:
        messagebox.showerror('Criação de Turma','Insira uma disciplina disponível no sistema!')
    elif verifica_turma() is False:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO turmas (cod, per, codd) VALUES (?,?,?)''',(ent_cad_cod_turm.get(),ent_cad_per_turm.get(),ent_cad_cod_disc_turm.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo('Criação de Turma', 'Turma criada com sucesso!')
    else:
        messagebox.showerror('Criação de Turma', 'A Turma já existe!')
def ver_disc_att_turma():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT codigo FROM disciplinas WHERE codigo = ?''',(ent_att_cod_disc_turm.get(),))
    if cursor.fetchone() is None:
        return False
    else:
        return True
def att_turma():
    if ver_disc_att_turma() is False:
        messagebox.showerror('Atualização de Turma', 'Insira uma disciplina disponível no sistema!')
    else:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''UPDATE turmas SET cod=?,per=?,codd=? WHERE cod=?  ''', (
        ent_att_cod_novo_turm.get(), ent_att_per_turm.get(), ent_att_cod_disc_turm.get(), ent_att_cod_turm.get(),))
        conn.commit()
        conn.close()
def rem_turm():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM turmas WHERE cod=?  ''', (ent_rem_turm.get(),))
    conn.commit()
    conn.close()
def att_cpf():
    frame_att_turm_insert.place(x=0,y=0)
    frame_att_turm.place(x=10000,y=0)
def turm_add_bd_cpfs():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE turmas SET cpfp = ?, cpfa = ? WHERE cod = ?'''.format(ent_cad_cod_turm.get()),('-'.join(lista_p),'-'.join(lista_a),ent_cad_cod_turm.get()))
    conn.commit()
    conn.close()
    aviso_turm_insert2['text'] = ''
    aviso_turm_insert3['text'] = ''
    aviso_turm_insert4['text'] = ''
    aviso_turm_insert5['text'] = ''
    messagebox.showinfo('Cadastro', 'CPFs Inseridos com sucesso!')
    if len(lista_p) > 0:
        for i in lista_p:
            lista_p.remove(i)
    if len(lista_a) > 0:
        for i in lista_a:
            lista_a.remove(i)
def add_prof_turm():
    if verifica_cpf_cad_turm_prof() == False:
        messagebox.showerror('Criação de Turmas', 'Insira um CPF válido!')
    elif ver_cad_turm_prof1() == True:
        if cpf_prof_turm.get() not in lista_p:
            lista_p.append(cpf_prof_turm.get())
            aviso_turm_insert2['text'] = '✔'
            aviso_turm_insert2['foreground'] = 'limegreen'
            aviso_turm_insert3['text'] = 'Professor adicionado com sucesso!'
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO relatorioprof  (cpf, per, disciplina, turma) VALUES (?,?,?,?) ''', (
            cpf_prof_turm.get(), ent_cad_per_turm.get(), ent_cad_cod_disc_turm.get(), ent_cad_cod_turm.get(),))
            conn.commit()
            conn.close()
            cpf_prof_turm.delete(0, END)
        else:
            aviso_turm_insert2['text'] = '✘'
            aviso_turm_insert2['foreground'] = 'red'
            aviso_turm_insert3['text'] = 'Professor já cadastrado!'
    else:
        aviso_turm_insert2['text'] = '✘'
        aviso_turm_insert2['foreground'] = 'red'
        aviso_turm_insert3['text'] = 'CPF não encontrado!'
        messagebox.showerror('Criação de Turmas', 'Insira um CPF disponível no sistema!')
def add_alun_turm():
    if verifica_cpf_cad_turm_aluno() == False:
        messagebox.showerror('Criação de Turmas', 'Insira um CPF válido!')
    elif ver_cad_turm_alun1() == True:
        if cpf_alun_turm.get() not in lista_a:
            lista_a.append(cpf_alun_turm.get())
            aviso_turm_insert4['text'] = '✔'
            aviso_turm_insert4['foreground'] = 'limegreen'
            aviso_turm_insert5['text'] = 'Aluno adicionado com sucesso!'
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO relatorioaluno  (cpf, per, disciplina, turma) VALUES (?,?,?,?) ''', (
                cpf_alun_turm.get(), ent_cad_per_turm.get(), ent_cad_cod_disc_turm.get(), ent_cad_cod_turm.get(),))
            conn.commit()
            conn.close()
            cpf_alun_turm.delete(0, END)
        else:
            aviso_turm_insert4['text'] = '✘'
            aviso_turm_insert4['foreground'] = 'red'
            aviso_turm_insert5['text'] = 'Aluno já cadastrado!'
    else:
        messagebox.showerror('Criação de Turmas', 'Insira um CPF disponível no sistema!')
        aviso_turm_insert4['text'] = '✘'
        aviso_turm_insert4['foreground'] = 'red'
        aviso_turm_insert5['text'] = 'CPF não encontrado!'
def vlt_cad_turm():
    ent_cad_per_turm.delete(0, END)
    ent_cad_cod_disc_turm.delete(0,END)
    ent_cad_cod_turm.delete(0,END)
    frame_cad_turm.place(x=10000, y=0)
    frame_turm.place(x=0, y=0)
def vlt_cons_turm():
    txt_cons_turm1['text'] = ''
    txt_cons_turm2['text'] = ''
    ent_cons_cod_turm.delete(0,END)
    lista_cons_turm.delete(0, END)
    frame_cons_turm.place(x=10000, y=0)
    frame_turm.place(x=0, y=0)
def vlt_rem_turm():
    ent_rem_turm.delete(0,END)
    frame_rem_turm.place(x=10000, y=0)
    frame_turm.place(x=0, y=0)
def vlt_att_turm():
    check_att_turm['text'] = ''
    ent_att_cod_turm.delete(0,END)
    ent_att_cod_disc_turm.delete(0,END)
    ent_att_per_turm.delete(0,END)
    ent_att_cod_novo_turm.delete(0,END)
    ent_att_cod_disc_turm['state'] = 'disabled'
    ent_att_per_turm['state'] = 'disabled'
    ent_att_cod_novo_turm['state'] = 'disabled'
    frame_att_turm.place(x=10000, y=0)
    frame_turm.place(x=0, y=0)
def vlt_turm_menu():
    frame_turm.place(x=10000, y=0)
    frame_principal.place(x=0, y=0)
def vlt_ata_turm():
    ent_ata_turm_cod.delete(0,END)
    lista_ata_turm.delete(0,END)
    frame_ata_turm.place(x=10000,y=0)
    frame_turm.place(x=0,y=0)
def vlt_att_cpf_turm():
    cpf_alun_att_turm.delete(0,END)
    cpf_prof_att_turm.delete(0,END)
    if len(lista_p)>0:
        for i in lista_p:
            lista_p.remove(i)
    if len(lista_a) > 0:
        for i in lista_a:
            lista_a.remove(i)
    frame_att_turm_insert.place(x=10000,y=0)
    frame_att_turm.place(x=0,y=0)
def vlt_insert_turm():
    cpf_alun_turm.delete(0,END)
    cpf_prof_turm.delete(0,END)
    aviso_turm_insert2['text'] = ''
    aviso_turm_insert3['text'] = ''
    aviso_turm_insert4['text'] = ''
    aviso_turm_insert5['text'] = ''
    if len(lista_p) > 0:
        for i in lista_p:
            lista_p.remove(i)
    if len(lista_a) > 0:
        for i in lista_a:
            lista_a.remove(i)
    frame_cad_turm_insert.place(x=10000,y=0)
    frame_cad_turm.place(x=0,y=0)

janela = Tk()
janela.geometry('640x480+500+180')
janela.maxsize(width='640', height='480')
janela.configure(background='royalblue4')
janela.iconbitmap('icon_ufrpe.ico')
janela.title('S.A.S')

# Frame do menu principal
frame_principal = Frame(janela, width='640', height='480', bg='gray15')
frame_principal.propagate(0)
frame_principal.place(x=0, y=0)
ttl_principal = Label(frame_principal, text='Sistema Acadêmico Simplificado', font=('System', '20', 'bold'), fg='goldenrod',
                      bg='gray15')
ttl_principal.pack(side='top')
espaco = Label(frame_principal, text='', bg='gray15', fg='dodgerblue1', font='System 16 underline')
espaco.pack()
txt_principal = Label(frame_principal, text='Escolha a opção desejada: ', bg='gray15', fg='goldenrod',
                      font=('System', '15'))
txt_principal.pack()
bt_principal0 = Button(frame_principal, text='Professores', font=('Terminal', '15'), fg='goldenrod', bg='gray25',
                       height='1', width='13', command=professor)
bt_principal1 = Button(frame_principal, text='Alunos', font=('Terminal', '15'), fg='goldenrod', bg='gray25', height='1',
                       width='13', command=aluno)
bt_principal2 = Button(frame_principal, text='Disciplinas', font=('Terminal', '15'), fg='goldenrod', bg='gray25',
                       height='1', width='13', command=disciplina)
bt_principal3 = Button(frame_principal, text='Turmas', font=('Terminal', '15'), fg='goldenrod', bg='gray25', height='1',
                       width='13', command=turma)
bt_principal4 = Button(frame_principal, text='Sair', font=('Terminal', '15'), fg='goldenrod', bg='gray25', height='1',
                       width='10', command=janela.quit)
textinho = Label(frame_principal, text='#_<BSI / UFRPE / IP2019.2>_#', font='Arial 7 bold', fg='darkolivegreen', bg='gray15')
bt_principal0.place(x=80, y=140)
bt_principal1.place(x=80, y=240)
bt_principal2.place(x=400, y=140)
bt_principal3.place(x=400, y=240)
bt_principal4.place(x=260, y=320)
textinho.place(x=0, y=465)

# Frame geral professores
frame_prof = Frame(janela, bg='gray15', width='640', height='480')
frame_prof.propagate(0)
frame_prof.place(x=10000, y=0)
ttl_prof = Label(frame_prof, text='Ações disponíveis para professores', font='System 20 bold', fg='goldenrod',
                 bg='gray15')
ttl_prof.pack(side='top')
espaco1 = Label(frame_prof, text='', bg='gray15', fg='goldenrod', font='System 16 underline')
espaco1.pack()
txt_prof = Label(frame_prof, text='Escolha a opção desejada em professores:', bg='gray15', fg='goldenrod',
                 font='System 16')
txt_prof.pack()
bt_prof = Button(frame_prof, text='Consultar', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                 width='13', command=consulta_prof)
bt_prof1 = Button(frame_prof, text='Cadastrar', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                  width='13', command=cadastro_prof)
bt_prof2 = Button(frame_prof, text='Atualizar', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                  width='13', command=atualizar_prof)
bt_prof3 = Button(frame_prof, text='Remover', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                  width='13', command=remover_prof)
bt_prof4 = Button(frame_prof, text='Relatórios', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                  width='13', command=relatorio_prof)
bt_prof5 = Button(frame_prof, text='Voltar', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                  width='10', command=vlt_prof_menu)
bt_prof.place(x=80, y=140)
bt_prof1.place(x=80, y=240)
bt_prof2.place(x=400, y=140)
bt_prof3.place(x=400, y=240)
bt_prof4.place(x=235, y=320)
bt_prof5.place(x=250, y=390)


# Frame cadastro professores
frame_cad_prof = Frame(janela, bg='gray15', width='640', height='480')
frame_cad_prof.propagate(0)
frame_cad_prof.place(x=10000, y=0)
ttl_cad_prof = Label(frame_cad_prof, text='Cadastro de Professores', font='System 20 bold', fg='goldenrod', bg='gray15')
ttl_cad_prof.pack()
ent_cad_nome_prof = Entry(frame_cad_prof, font='System 15', fg='gray15', bg='gray70', width='30')
ent_cad_nome_prof.place(x=220, y=100)
nome_prof = Label(frame_cad_prof, text='Nome:', font='System 15', fg='goldenrod', bg='gray15')
nome_prof.place(x=100, y=100)
cpf_prof = Label(frame_cad_prof, text='CPF:', font='System 15', fg='goldenrod', bg='gray15')
cpf_prof.place(x=100, y=140)
ent_cad_cpf_prof = Entry(frame_cad_prof, font='System 15', fg='gray10', bg='gray70', width='30')
ent_cad_cpf_prof.place(x=220, y=140)
dep_prof = Label(frame_cad_prof, text='Departamento:', font='System 15', fg='goldenrod', bg='gray15')
dep_prof.place(x=100, y=180)
ent_cad_dep_prof = Entry(frame_cad_prof, font='System 15', fg='gray10', bg='gray70', width='30')
ent_cad_dep_prof.place(x=220, y=180)
bt_cad_prof = Button(frame_cad_prof, text='Cadastrar', font='System 15', fg='goldenrod', bg='gray25',
                     command=cad_prof)
bt_cad_prof.place(x=290, y=300)
bt_volta_prof = Button(frame_cad_prof, text='Voltar', font='System 15', fg='goldenrod', bg='gray25',
                       command=vlt_cad_prof)
bt_volta_prof.place(x=395, y=300)

# Frame consulta professores
frame_cons_prof = Frame(janela, bg='gray15', width='640', height='480')
frame_cons_prof.propagate(0)
frame_cons_prof.place(x=10000, y=0)
ttl_cons_prof = Label(frame_cons_prof, text='Consulta de Professores', font='System 20 bold', fg='goldenrod', bg='gray15')
ttl_cons_prof.pack()
ent_cons_cpf_prof = Entry(frame_cons_prof, font='System 15', fg='gray10', bg='gray70', width='18')
ent_cons_cpf_prof.place(x=280, y=60)
txt_cons_prof = Label(frame_cons_prof, text='CPF:', font='System 15', fg='goldenrod', bg='gray15')
txt_cons_prof.place(x=220, y=60)
txt_cons_prof1 = Label(frame_cons_prof, text='', font='System 15', fg='goldenrod', bg='gray15')
txt_cons_prof1.place(x=260, y=275)
txt_cons_prof2 = Label(frame_cons_prof, text='', font='System 15', fg='red', bg='gray15')
txt_cons_prof2.place(x=235, y=273)
lista_cons_prof = Listbox(frame_cons_prof,selectbackground= 'gray15',  font='System 15', width='50', height='10',
                                            bg='gray70', fg='gray10')
lista_cons_prof.place(x=120, y=100)
bt_cons_prof = Button(frame_cons_prof, text='Consultar', font='System 15', fg='goldenrod', bg='gray25',
                      command=cons_prof)
bt_cons_prof.place(x=250, y=300)
bt_volta_prof = Button(frame_cons_prof, text='Voltar', font='System 15', fg='goldenrod', bg='gray25',
                       command=vlt_cons_prof)
bt_volta_prof.place(x=350, y=300)

# Frame atualizar professores
frame_att_prof = Frame(janela, bg='gray15', width='640', height='480')
frame_att_prof.propagate(0)
frame_att_prof.place(x=10000, y=0)
cont_att_prof_info = Frame(frame_att_prof, bg='gray15', widt='350', height='300')
cont_att_prof_info.place(x=140, y=80)
ttl_att_prof = Label(frame_att_prof, text='Atualização de Professores', font='System 20 bold', fg='goldenrod', bg='gray15')
ttl_att_prof.pack()
txt_att_prof = Label(cont_att_prof_info, text='CPF:', font='System 15', fg='goldenrod', bg='gray15')
txt_att_prof.place(x=0, y=25)
ent_att_cpf_antigo_prof = Entry(cont_att_prof_info, font='System 15', fg='gray10', bg='gray70', width='15')
ent_att_cpf_antigo_prof.place(x=40, y=25)
txt_att_prof1 = Label(cont_att_prof_info, text='Confira e atualize as informações desejadas abaixo:', font='System 15',
                      fg='gray70', bg='gray15')
txt_att_prof1.place(x=0, y=65)
txt_att_prof2 = Label(cont_att_prof_info, text='Insira o CPF do professor que será atualizado:', font='System 15',
                      fg='gray70', bg='gray15')
txt_att_prof2.place(x=0, y=0)
ent_att_nome_novo_prof = Entry(cont_att_prof_info, state='disabled', font='System 15', fg='gray10', bg='gray70', width='25')
ent_att_nome_novo_prof.place(x=50, y=98)
ent_att_cpf_novo_prof = Entry(cont_att_prof_info, font='System 15', state='disabled', fg='gray10', bg='gray70', width='15')
ent_att_cpf_novo_prof.place(x=50, y=128)
ent_att_dep_novo_prof = Entry(cont_att_prof_info, font='System 15', state='disabled', fg='gray10', bg='gray70', width='15')
ent_att_dep_novo_prof.place(x=50, y=158)
prof_nome = Label(cont_att_prof_info, text='Nome:', font='System 15 bold', fg='goldenrod', bg='gray15')
prof_nome.place(x=0, y=95)
prof_cpf = Label(cont_att_prof_info, text='CPF:', font='System 15 bold', fg='goldenrod', bg='gray15')
prof_cpf.place(x=0, y=125)
prof_dep = Label(cont_att_prof_info, text='Dept:', font='System 15 bold', fg='goldenrod', bg='gray15')
prof_dep.place(x=0, y=155)
btt_att_ver_prof = Button(cont_att_prof_info, text='Verificar', font='System 15', fg='goldenrod', bg='gray25',
                          command=ver_att_prof)
btt_att_ver_prof.place(x=180, y=20)
ver_att_prof = Label(cont_att_prof_info, text='', font='System 20', fg='limegreen', bg='gray15')
ver_att_prof.place(x=250, y=16)
btt_att_prof = Button(cont_att_prof_info, text='Atualizar', font='System 15', fg='goldenrod', bg='gray25',
                      command=att_prof)
btt_att_prof.place(x=120, y=270)
bt_volta_prof = Button(cont_att_prof_info, text='Voltar', font='System 15', fg='goldenrod', bg='gray25',
                       command=vlt_att_prof)
bt_volta_prof.place(x=200, y=270)

# Frame remover professores
frame_rem_prof = Frame(janela, bg='gray15', width='640', height='480')
frame_rem_prof.propagate(0)
frame_rem_prof.place(x=10000, y=0)
ttl_rem_prof = Label(frame_rem_prof, text='Remoção de Professores', font='System 20 bold', fg='goldenrod', bg='gray15')
ttl_rem_prof.pack()
esp = Label(frame_rem_prof, text='', font='System 15 bold', fg='gray70', bg='gray15')
esp.pack()
txt_rem_prof = Label(frame_rem_prof, text='Informe o CPF do cadastro que você deseja excluir:', font='System 15 bold',
                     fg='gray70', bg='gray15')
txt_rem_prof.pack()
txt_rem_prof1 = Label(frame_rem_prof, text='CPF:', font='System 15 bold', fg='goldenrod', bg='gray15')
txt_rem_prof1.place(x=200, y=120)
ent_rem_prof = Entry(frame_rem_prof, font='System 15', fg='gray10', bg='gray70')
ent_rem_prof.place(x=250, y=120)
bt_rem_prof = Button(frame_rem_prof, text='Deletar', font='System 15', fg='goldenrod', bg='gray25', command=rem_prof)
bt_rem_prof.place(x=250, y=300)
bt_volta_prof = Button(frame_rem_prof, text='Voltar', font='System 15', fg='goldenrod', bg='gray25',
                       command=vlt_rem_prof)
bt_volta_prof.place(x=335, y=300)

# Frame relatório de professores

frame_rel_prof = Frame(janela, bg='gray15', width='640', height='480')
frame_rel_prof.propagate(0)
frame_rel_prof.place(x=10000,y=0)
ttl_rel_prof = Label(frame_rel_prof, text='Relatórios de Professores', font='System 20 bold', fg='goldenrod',
                 bg='gray15')
ttl_rel_prof.pack(side='top')
txt_rel_prof_cpf = Label(frame_rel_prof, text='CPF: ', font='System 15', fg='goldenrod', bg='gray15')
txt_rel_prof_cpf.place(x=160, y=75)
txt_rel_prof_per = Label(frame_rel_prof, text='Período: ', font='System 15', fg='goldenrod', bg='gray15')
txt_rel_prof_per.place(x=135,y=100)
ent_rel_prof_cpf = Entry(frame_rel_prof, font='System 15', fg='gray10', bg='gray70')
ent_rel_prof_cpf.place(x=200, y=75)
ent_rel_prof_per = Entry(frame_rel_prof, font='System 15', fg='gray10', bg='gray70')
ent_rel_prof_per.place(x=200, y=100)
lista_rel_prof = Listbox(frame_rel_prof,selectbackground= 'gray15', font='System 15', fg='gray10', bg='gray70', width='50', height='15')
lista_rel_prof.place(x=120,y=140)
bt_rel_prof = Button(frame_rel_prof, text='Gerar', font='System 15', fg='goldenrod', bg='gray25', command=rel_prof)
bt_rel_prof.place(x=350, y=420)
bt_volta_prof = Button(frame_rel_prof, text='Voltar', font='System 15', fg='goldenrod', bg='gray25', command=vlt_rel_prof)
bt_volta_prof.place(x=435, y=420)

# Frame geral alunos
frame_alun = Frame(janela, bg='gray15', width='640', height='480')
frame_alun.propagate(0)
frame_alun.place(x=10000, y=0)
ttl_alun = Label(frame_alun, text='Ações disponíveis para alunos', font='System 20 bold', fg='goldenrod',
                 bg='gray15')
ttl_alun.pack(side='top')
espaco1 = Label(frame_alun, text='', bg='gray15', fg='goldenrod', font='System 16 underline')
espaco1.pack()
txt_alun = Label(frame_alun, text='Escolha a opção desejada em alunos:', bg='gray15', fg='goldenrod',
                 font='System 16')
txt_alun.pack()
bt_alun = Button(frame_alun, text='Consultar', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                 width='13', command=consulta_aluno)
bt_alun1 = Button(frame_alun, text='Cadastrar', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                  width='13', command=cadastro_aluno)
bt_alun2 = Button(frame_alun, text='Atualizar', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                  width='13', command=atualizar_aluno)
bt_alun3 = Button(frame_alun, text='Remover', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                  width='13', command=remover_aluno)
bt_alun4 = Button(frame_alun, text='Relatórios', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                  width='13', command=relatorio_alun)
bt_alun5 = Button(frame_alun, text='Voltar', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                  width='10', command=vlt_alun_menu)
bt_alun.place(x=80, y=140)
bt_alun1.place(x=80, y=240)
bt_alun2.place(x=400, y=140)
bt_alun3.place(x=400, y=240)
bt_alun4.place(x=235, y=320)
bt_alun5.place(x=250, y=390)


# Frame cadastro alunos
frame_cad_alun = Frame(janela, bg='gray15', width='640', height='480')
frame_cad_alun.propagate(0)
frame_cad_alun.place(x=10000, y=0)
ttl_cad_alun = Label(frame_cad_alun, text='Cadastro de Alunos', font='System 20 bold', fg='goldenrod', bg='gray15')
ttl_cad_alun.pack()
ent_cad_nome_alun = Entry(frame_cad_alun, font='System 15', fg='gray15', bg='gray70', width='30')
ent_cad_nome_alun.place(x=220, y=100)
nome_alun = Label(frame_cad_alun, text='Nome:', font='System 15', fg='goldenrod', bg='gray15')
nome_alun.place(x=100, y=100)
cpf_alun = Label(frame_cad_alun, text='CPF:', font='System 15', fg='goldenrod', bg='gray15')
cpf_alun.place(x=100, y=140)
ent_cad_cpf_alun = Entry(frame_cad_alun, font='System 15', fg='gray10', bg='gray70', width='30')
ent_cad_cpf_alun.place(x=220, y=140)
bt_cad_alun = Button(frame_cad_alun, text='Cadastrar', font='System 15', fg='goldenrod', bg='gray25',
                     command=cad_aluno)
bt_cad_alun.place(x=290, y=300)
bt_volta_alun = Button(frame_cad_alun, text='Voltar', font='System 15', fg='goldenrod', bg='gray25',
                       command=vlt_cad_alun)
bt_volta_alun.place(x=395, y=300)

# Frame consulta alunos
frame_cons_alun = Frame(janela, bg='gray15', width='640', height='480')
frame_cons_alun.propagate(0)
frame_cons_alun.place(x=10000, y=0)
ttl_cons_alun = Label(frame_cons_alun, text='Consulta de Alunos', font='System 20 bold', fg='goldenrod', bg='gray15')
ttl_cons_alun.pack()
ent_cons_cpf_alun = Entry(frame_cons_alun, font='System 15', fg='gray10', bg='gray70', width='18')
ent_cons_cpf_alun.place(x=280, y=60)
txt_cons_alun = Label(frame_cons_alun, text='CPF:', font='System 15', fg='goldenrod', bg='gray15')
txt_cons_alun.place(x=220, y=60)
txt_cons_alun1 = Label(frame_cons_alun, text='', font='System 15', fg='goldenrod', bg='gray15')
txt_cons_alun1.place(x=260, y=275)
txt_cons_alun2 = Label(frame_cons_alun, text='', font='System 15', fg='red', bg='gray15')
txt_cons_alun2.place(x=235, y=273)
lista_cons_alun = Listbox(frame_cons_alun, selectbackground= 'gray15', font='System 15', width='50', height='10',
                                            bg='gray70', fg='gray10')
lista_cons_alun.place(x=120, y=100)
bt_cons_alun = Button(frame_cons_alun, text='Consultar', font='System 15', fg='goldenrod', bg='gray25',
                      command=cons_alun)
bt_cons_alun.place(x=250, y=300)
bt_volta_alun = Button(frame_cons_alun, text='Voltar', font='System 15', fg='goldenrod', bg='gray25',
                       command=vlt_cons_alun)
bt_volta_alun.place(x=350, y=300)

# Frame atualizar alunos
frame_att_alun = Frame(janela, bg='gray15', width='640', height='480')
frame_att_alun.propagate(0)
frame_att_alun.place(x=10000, y=0)
cont_att_alun_info = Frame(frame_att_alun, bg='gray15', widt='350', height='300')
cont_att_alun_info.place(x=180, y=80)
ttl_att_alun = Label(frame_att_alun, text='Atualização de Alunos', font='System 20 bold', fg='goldenrod', bg='gray15')
ttl_att_alun.pack()
txt_att_alun = Label(cont_att_alun_info, text='CPF:', font='System 15', fg='goldenrod', bg='gray15')
txt_att_alun.place(x=0, y=25)
ent_att_cpf_antigo_alun = Entry(cont_att_alun_info, font='System 15', fg='gray10', bg='gray70', width='15')
ent_att_cpf_antigo_alun.place(x=40, y=25)
txt_att_alun1 = Label(cont_att_alun_info, text='Verifique e altere as informações abaixo:', font='System 15',
                      fg='gray70', bg='gray15')
txt_att_alun1.place(x=0, y=65)
txt_att_alun2 = Label(cont_att_alun_info, text='Insira o CPF do aluno que será atualizado:', font='System 15',
                      fg='gray70', bg='gray15')
txt_att_alun2.place(x=0, y=0)
ent_att_nome_novo_alun = Entry(cont_att_alun_info, state='disabled', font='System 15', fg='gray10', bg='gray70', width='25')
ent_att_nome_novo_alun.place(x=50, y=98)
ent_att_cpf_novo_alun = Entry(cont_att_alun_info, state='disabled', font='System 15', fg='gray10', bg='gray70', width='15')
ent_att_cpf_novo_alun.place(x=50, y=128)
alun_nome = Label(cont_att_alun_info, text='Nome:', font='System 15 bold', fg='goldenrod', bg='gray15')
alun_nome.place(x=0, y=95)
alun_cpf = Label(cont_att_alun_info, text='CPF:', font='System 15 bold', fg='goldenrod', bg='gray15')
alun_cpf.place(x=0, y=125)
btt_att_ver_alun = Button(cont_att_alun_info, text='Verificar', font='System 15', fg='goldenrod', bg='gray25',
                          command=ver_att_alun)
btt_att_ver_alun.place(x=180, y=20)
ver_att_alun = Label(cont_att_alun_info, text='', font='System 20', fg='limegreen', bg='gray15')
ver_att_alun.place(x=250, y=16)
btt_att_alun = Button(cont_att_alun_info, text='Atualizar', font='System 15', fg='goldenrod', bg='gray25',
                      command=att_alun)
btt_att_alun.place(x=80, y=270)
bt_volta_alun = Button(cont_att_alun_info, text='Voltar', font='System 15', fg='goldenrod', bg='gray25',
                       command=vlt_att_alun)
bt_volta_alun.place(x=160, y=270)
# Frame remover alunos
frame_rem_alun = Frame(janela, bg='gray15', width='640', height='480')
frame_rem_alun.propagate(0)
frame_rem_alun.place(x=10000, y=0)
ttl_rem_alun = Label(frame_rem_alun, text='Remoção de Alunos', font='System 20 bold', fg='goldenrod', bg='gray15')
ttl_rem_alun.pack()
esp = Label(frame_rem_alun, text='', font='System 15 bold', fg='gray70', bg='gray15')
esp.pack()
txt_rem_alun = Label(frame_rem_alun, text='Informe o CPF do cadastro que você deseja excluir:', font='System 15 bold',
                     fg='gray70', bg='gray15')
txt_rem_alun.pack()
txt_rem_alun1 = Label(frame_rem_alun, text='CPF:', font='System 15 bold', fg='goldenrod', bg='gray15')
txt_rem_alun1.place(x=200, y=120)
ent_rem_alun = Entry(frame_rem_alun, font='System 15', fg='gray10', bg='gray70')
ent_rem_alun.place(x=250, y=120)
bt_rem_alun = Button(frame_rem_alun, text='Deletar', font='System 15', fg='goldenrod', bg='gray25', command=rem_alun)
bt_rem_alun.place(x=250, y=300)
bt_volta_alun = Button(frame_rem_alun, text='Voltar', font='System 15', fg='goldenrod', bg='gray25',
                       command=vlt_rem_alun)
bt_volta_alun.place(x=335, y=300)

# Frame relatório de alunos

frame_rel_alun = Frame(janela, bg='gray15', width='640', height='480')
frame_rel_alun.propagate(0)
frame_rel_alun.place(x=10000,y=0)
ttl_rel_alun = Label(frame_rel_alun, text='Relatórios de Alunos', font='System 20 bold', fg='goldenrod',
                 bg='gray15')
ttl_rel_alun.pack(side='top')
txt_rel_alun_cpf = Label(frame_rel_alun, text='CPF: ', font='System 15', fg='goldenrod', bg='gray15')
txt_rel_alun_cpf.place(x=210, y=75)
txt_rel_alun_per = Label(frame_rel_alun, text='Período: ', font='System 15', fg='goldenrod', bg='gray15')
txt_rel_alun_per.place(x=185,y=100)
ent_rel_alun_cpf = Entry(frame_rel_alun, font='System 15', fg='gray10', bg='gray70')
ent_rel_alun_cpf.place(x=250, y=75)
ent_rel_alun_per = Entry(frame_rel_alun, font='System 15', fg='gray10', bg='gray70')
ent_rel_alun_per.place(x=250, y=100)
lista_rel_alun = Listbox(frame_rel_alun,selectbackground= 'gray15', font='System 15', fg='gray10', bg='gray70', width='50', height='15')
lista_rel_alun.place(x=120,y=140)
bt_rel_alun = Button(frame_rel_alun, text='Gerar', font='System 15', fg='goldenrod', bg='gray25', command=rel_alun)
bt_rel_alun.place(x=350, y=420)
bt_volta_alun = Button(frame_rel_alun, text='Voltar', font='System 15', fg='goldenrod', bg='gray25', command=vlt_rel_alun)
bt_volta_alun.place(x=435, y=420)

# Frame geral disciplinas
frame_disc = Frame(janela, bg='gray15', width='640', height='480')
frame_disc.propagate(0)
frame_disc.place(x=10000, y=0)
ttl_disc = Label(frame_disc, text='Ações disponíveis para disciplinas', font='System 20 bold', fg='goldenrod',
                 bg='gray15')
ttl_disc.pack(side='top')
espaco1 = Label(frame_disc, text='', bg='gray15', fg='goldenrod', font='System 16 underline')
espaco1.pack()
txt_disc = Label(frame_disc, text='Escolha a opção desejada em disciplinas:', bg='gray15', fg='goldenrod',
                 font='System 16')
txt_disc.pack()
bt_disc = Button(frame_disc, text='Consultar', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                 width='13', command=consulta_disc)
bt_disc1 = Button(frame_disc, text='Cadastro', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                  width='13', command=cadastro_disc)
bt_disc2 = Button(frame_disc, text='Atualizar', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                  width='13', command=atualizar_disc)
bt_disc3 = Button(frame_disc, text='Remover', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                  width='13', command=remover_disc)
bt_disc4 = Button(frame_disc, text='Voltar', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                  width='10', command=vlt_disc_menu)
bt_disc.place(x=80, y=140)
bt_disc1.place(x=80, y=240)
bt_disc2.place(x=400, y=140)
bt_disc3.place(x=400, y=240)
bt_disc4.place(x=260, y=320)

# Frame criar disciplina
frame_cad_disc = Frame(janela, bg='gray15', width='640', height='480')
frame_cad_disc.propagate(0)
frame_cad_disc.place(x=10000, y=0)
ttl_cad_disc = Label(frame_cad_disc, text='Cadastro de Disciplinas', font='System 20 bold', fg='goldenrod', bg='gray15')
ttl_cad_disc.pack()
ent_cad_nome_disc = Entry(frame_cad_disc, font='System 15', fg='gray10', bg='gray70', width='30')
ent_cad_nome_disc.place(x=220, y=100)
nome_disc = Label(frame_cad_disc, text='Nome:', font='System 15', fg='goldenrod', bg='gray15')
nome_disc.place(x=100, y=100)
cod_disc = Label(frame_cad_disc, text='Código:', font='System 15', fg='goldenrod', bg='gray15')
cod_disc.place(x=100, y=140)
ent_cad_cod_disc = Entry(frame_cad_disc, font='System 15', fg='gray10', bg='gray70', width='30')
ent_cad_cod_disc.place(x=220, y=140)
bt_cad_disc = Button(frame_cad_disc, text='Criar', font='System 15', fg='goldenrod', bg='gray25',
                     command=cad_disc)
bt_cad_disc.place(x=320, y=300)
bt_volta_disc = Button(frame_cad_disc, text='Voltar', font='System 15', fg='goldenrod', bg='gray25',
                       command=vlt_cad_disc)
bt_volta_disc.place(x=395, y=300)

# Frame consulta disciplinas
frame_cons_disc = Frame(janela, bg='gray15', width='640', height='480')
frame_cons_disc.propagate(0)
frame_cons_disc.place(x=10000, y=0)
ttl_cons_disc = Label(frame_cons_disc, text='Consulta de Disciplinas', font='System 20 bold', fg='goldenrod', bg='gray15')
ttl_cons_disc.pack()
ent_cons_cod_disc = Entry(frame_cons_disc, font='System 15', fg='gray10', bg='gray70', width='18')
ent_cons_cod_disc.place(x=280, y=60)
txt_cons_disc = Label(frame_cons_disc, text='Código:', font='System 15', fg='goldenrod', bg='gray15')
txt_cons_disc.place(x=220, y=60)
txt_cons_disc1 = Label(frame_cons_disc, text='', font='System 15', fg='goldenrod', bg='gray15')
txt_cons_disc1.place(x=260, y=275)
txt_cons_disc2 = Label(frame_cons_disc, text='', font='System 15', fg='red', bg='gray15')
txt_cons_disc2.place(x=235, y=273)
lista_cons_disc = Listbox(frame_cons_disc,selectbackground= 'gray15', font='System 15', width='50', height='10',
                                            bg='gray70', fg='gray10')
lista_cons_disc.place(x=120, y=100)
bt_cons_disc = Button(frame_cons_disc, text='Consultar', font='System 15', fg='goldenrod', bg='gray25',
                      command=cons_disc)
bt_cons_disc.place(x=250, y=300)
bt_volta_disc = Button(frame_cons_disc, text='Voltar', font='System 15', fg='goldenrod', bg='gray25',
                       command=vlt_cons_disc)
bt_volta_disc.place(x=350, y=300)
# Frame atualizar disciplinas
frame_att_disc = Frame(janela, bg='gray15', width='640', height='480')
frame_att_disc.propagate(0)
frame_att_disc.place(x=10000, y=0)
cont_att_disc_info = Frame(frame_att_disc, bg='gray15', widt='350', height='300')
cont_att_disc_info.place(x=140, y=80)
ttl_att_disc = Label(frame_att_disc, text='Atualização de Disciplinas', font='System 20 bold', fg='goldenrod', bg='gray15')
ttl_att_disc.pack()
txt_att_disc = Label(cont_att_disc_info, text='COD:', font='System 15', fg='goldenrod', bg='gray15')
txt_att_disc.place(x=0, y=25)
ent_att_cod_antigo_disc = Entry(cont_att_disc_info, font='System 15', fg='gray10', bg='gray70', width='15')
ent_att_cod_antigo_disc.place(x=40, y=25)
txt_att_disc1 = Label(cont_att_disc_info, text='Confira e atualize as informações desejadas abaixo:', font='System 15',
                      fg='gray70', bg='gray15')
txt_att_disc1.place(x=0, y=65)
txt_att_disc2 = Label(cont_att_disc_info, text='Insira o COD da disciplina que será atualizada:', font='System 15',
                      fg='gray70', bg='gray15')
txt_att_disc2.place(x=0, y=0)
ent_att_nome_novo_disc = Entry(cont_att_disc_info, state='disabled', font='System 15', fg='gray10', bg='gray70', width='25')
ent_att_nome_novo_disc.place(x=50, y=98)
ent_att_cod_novo_disc = Entry(cont_att_disc_info, state='disabled', font='System 15', fg='gray10', bg='gray70', width='15')
ent_att_cod_novo_disc.place(x=38, y=128)
disc_nome = Label(cont_att_disc_info, text='Nome:', font='System 15 bold', fg='goldenrod', bg='gray15')
disc_nome.place(x=0, y=95)
disc_cod = Label(cont_att_disc_info, text='COD:', font='System 15 bold', fg='goldenrod', bg='gray15')
disc_cod.place(x=0, y=125)
btt_att_ver_disc = Button(cont_att_disc_info, text='Verificar', font='System 15', fg='goldenrod', bg='gray25',
                          command=ver_att_disc)
btt_att_ver_disc.place(x=180, y=20)
ver_att_disc = Label(cont_att_disc_info, text='', font='System 20', fg='limegreen', bg='gray15')
ver_att_disc.place(x=250, y=16)
btt_att_disc = Button(cont_att_disc_info, text='Atualizar', font='System 15', fg='goldenrod', bg='gray25',
                      command=att_disc)
btt_att_disc.place(x=120, y=270)
bt_volta_disc = Button(cont_att_disc_info, text='Voltar', font='System 15', fg='goldenrod', bg='gray25',
                       command=vlt_att_disc)
bt_volta_disc.place(x=200, y=270)

# Frame remover disciplinas
frame_rem_disc = Frame(janela, bg='gray15', width='640', height='480')
frame_rem_disc.propagate(0)
frame_rem_disc.place(x=10000, y=0)
ttl_rem_disc = Label(frame_rem_disc, text='Remoção de Disciplinas', font='System 20 bold', fg='goldenrod', bg='gray15')
ttl_rem_disc.pack()
esp = Label(frame_rem_disc, text='', font='System 15 bold', fg='gray70', bg='gray15')
esp.pack()
txt_rem_disc = Label(frame_rem_disc, text='Informe o Código do cadastro que você deseja excluir:', font='System 15 bold',
                     fg='gray70', bg='gray15')
txt_rem_disc.pack()
txt_rem_disc1 = Label(frame_rem_disc, text='Código:', font='System 15 bold', fg='goldenrod', bg='gray15')
txt_rem_disc1.place(x=190, y=120)
ent_rem_disc = Entry(frame_rem_disc, font='System 15', fg='gray10', bg='gray70')
ent_rem_disc.place(x=250, y=120)
bt_rem_disc = Button(frame_rem_disc, text='Deletar', font='System 15', fg='goldenrod', bg='gray25', command=rem_disc)
bt_rem_disc.place(x=250, y=300)
bt_volta_disc = Button(frame_rem_disc, text='Voltar', font='System 15', fg='goldenrod', bg='gray25',
                       command=vlt_rem_disc)
bt_volta_disc.place(x=335, y=300)

# Frame geral turmas
frame_turm = Frame(janela, bg='gray15', width='640', height='480')
frame_turm.propagate(0)
frame_turm.place(x=10000, y=0)
ttl_turm = Label(frame_turm, text='Ações disponíveis para turmas', font='System 20 bold', fg='goldenrod',
                 bg='gray15')
ttl_turm.pack(side='top')
espaco1 = Label(frame_turm, text='', bg='gray15', fg='goldenrod', font='System 16 underline')
espaco1.pack()
txt_turm = Label(frame_turm, text='Escolha a opção desejada em turmas:', bg='gray15', fg='goldenrod',
                 font='System 16')
txt_turm.pack()
bt_turm = Button(frame_turm, text='Consultar', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                 width='13', command=consulta_turma)
bt_turm1 = Button(frame_turm, text='Cadastro', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                  width='13', command=cadastro_turma)
bt_turm2 = Button(frame_turm, text='Atualizar', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                  width='13', command=atualizar_turma)
bt_turm3 = Button(frame_turm, text='Remover', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                  width='13', command=remover_turma)
bt_turm4 = Button(frame_turm, text='Atas', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                  width='13', command=ata_turma)
bt_turm5 = Button(frame_turm, text='Voltar', font='Terminal 15', fg='goldenrod', bg='gray25', height='1',
                  width='10', command=vlt_turm_menu)
bt_turm.place(x=80, y=140)
bt_turm1.place(x=80, y=240)
bt_turm2.place(x=400, y=140)
bt_turm3.place(x=400, y=240)
bt_turm4.place(x=235, y=320)
bt_turm5.place(x=250, y=390)

# Frame criar turmas
frame_cad_turm = Frame(janela, bg='gray15', width='640', height='480')
frame_cad_turm.propagate(0)
frame_cad_turm.place(x=10000, y=0)
ttl_cad_turm = Label(frame_cad_turm, text='Cadastro de Turma', font='System 20 bold', fg='goldenrod', bg='gray15')
ttl_cad_turm.pack()
ent_cad_cod_turm = Entry(frame_cad_turm, font='System 15', fg='gray10', bg='gray70', width='30')
ent_cad_cod_turm.place(x=220, y=100)
nome_turm = Label(frame_cad_turm, text='Código da turma:', font='System 15', fg='goldenrod', bg='gray15')
nome_turm.place(x=75, y=100)
cod_turm = Label(frame_cad_turm, text='Código da Disciplina:', font='System 15', fg='goldenrod', bg='gray15')
cod_turm.place(x=75, y=140)
per_turm = Label(frame_cad_turm, text='Período:', font='System 15', fg='goldenrod', bg='gray15')
per_turm.place(x=75, y=180)
ent_cad_cod_disc_turm = Entry(frame_cad_turm, font='System 15', fg='gray10', bg='gray70', width='30')
ent_cad_cod_disc_turm.place(x=220, y=140)
ent_cad_per_turm = Entry(frame_cad_turm, font='System 15', fg='gray10', bg='gray70', width='30')
ent_cad_per_turm.place(x=220, y=180)
aviso_turm = Label(frame_cad_turm, text='⚠', font='System 15', fg='red', bg='gray15')
aviso_turm.place(x=165, y=348)
aviso_turm1 = Label(frame_cad_turm, text='Criar a turma antes de inserir os CPFs', font='System 15', fg='goldenrod', bg='gray15')
aviso_turm1.place(x=190, y=350)
bt_cad_turm = Button(frame_cad_turm, text='Criar', font='System 15', fg='goldenrod', bg='gray25',
                     command=cad_turma)
bt_cad_turm.place(x=220, y=300)
bt_volta_turm = Button(frame_cad_turm, text='Voltar', font='System 15', fg='goldenrod', bg='gray25',
                       command=vlt_cad_turm)
bt_insert_cpf = Button(frame_cad_turm, text='Inserir CPFS', font='System 15', fg='goldenrod', bg='gray25',
                       command=insert_cpf)
bt_volta_turm.place(x=410, y=300)
bt_insert_cpf.place(x=290, y=300)

# Frame inserir aluno e professor
frame_cad_turm_insert = Frame(janela, bg='gray15', width='640', height='480')
frame_cad_turm_insert.propagate(0)
frame_cad_turm_insert.place(x=10000, y=0)
ttl_cad_turm_insert = Label(frame_cad_turm_insert, text='Inserir CPFS', font='System 20 bold', fg='goldenrod', bg='gray15')
ttl_cad_turm_insert.pack()
cpf_prof_turm = Entry(frame_cad_turm_insert, font='System 15', fg='gray10', bg='gray70', width='30')
cpf_prof_turm.place(x=220, y=100)
txt_cpf_prof_turm = Label(frame_cad_turm_insert, text='Professor:', font='System 15', fg='goldenrod', bg='gray15')
txt_cpf_prof_turm.place(x=75, y=100)
cpf_alun_turm = Entry(frame_cad_turm_insert, font='System 15', fg='gray10', bg='gray70', width='30')
cpf_alun_turm.place(x=220, y=160)
aviso_turm_insert = Label(frame_cad_turm_insert, text='⚠', font='System 15', fg='red', bg='gray15')
aviso_turm_insert.place(x=110, y=58)
aviso_turm_insert1 = Label(frame_cad_turm_insert, text='Após adicionar os CPFs, pressionar o botão CADASTRAR!', font='System 15', fg='goldenrod', bg='gray15')
aviso_turm_insert1.place(x=140, y=60)
aviso_turm_insert2 = Label(frame_cad_turm_insert, text='', font='System 15', fg='red', bg='gray15')
aviso_turm_insert2.place(x=200, y=123)
aviso_turm_insert3 = Label(frame_cad_turm_insert, text='', font='System 15', fg='goldenrod', bg='gray15')
aviso_turm_insert3.place(x=230, y=125)
aviso_turm_insert4 = Label(frame_cad_turm_insert, text='', font='System 15', fg='red', bg='gray15')
aviso_turm_insert4.place(x=220, y=183)
aviso_turm_insert5 = Label(frame_cad_turm_insert, text='', font='System 15', fg='goldenrod', bg='gray15')
aviso_turm_insert5.place(x=250, y=185)
aviso_turm_insert6 = Label(frame_cad_turm_insert, text='Quantidade de professores na turma:', font='System 15', fg='goldenrod', bg='gray15')
aviso_turm_insert6.place(x=200, y=360)
aviso_turm_insert7 = Label(frame_cad_turm_insert, text='0', font='System 15', fg='red', bg='gray15')
aviso_turm_insert7.place(x=450, y=360)
aviso_turm_insert8 = Label(frame_cad_turm_insert, text='Quantidade de alunos na turma:', font='System 15', fg='goldenrod', bg='gray15')
aviso_turm_insert8.place(x=200, y=390)
aviso_turm_insert9 = Label(frame_cad_turm_insert, text='0', font='System 15', fg='red', bg='gray15')
aviso_turm_insert9.place(x=410, y=390)
txt_cpf_alun_turm = Label(frame_cad_turm_insert, text='Aluno:', font='System 15', fg='goldenrod', bg='gray15')
txt_cpf_alun_turm.place(x=75, y=160)
bt_add_prof = Button(frame_cad_turm_insert, text='Add prof', font='System 15', fg='goldenrod', bg='gray25',
                       command=add_prof_turm)
bt_add_alun = Button(frame_cad_turm_insert, text='Add aluno', font='System 15', fg='goldenrod', bg='gray25',
                       command=add_alun_turm)
bt_volta_turm = Button(frame_cad_turm_insert, text='Voltar', font='System 15', fg='goldenrod', bg='gray25',
                       command=vlt_insert_turm)
bt_insert_cpf = Button(frame_cad_turm_insert, text='Cadastrar', font='System 15', fg='goldenrod', bg='gray25',
                       command=turm_add_bd_cpfs)
bt_add_prof.place(x=480, y=95)
bt_add_alun.place(x=480, y=155)
bt_volta_turm.place(x=410, y=300)
bt_insert_cpf.place(x=290, y=300)


# Frame consulta turmas
frame_cons_turm = Frame(janela, bg='gray15', width='640', height='480')
frame_cons_turm.propagate(0)
frame_cons_turm.place(x=10000, y=0)
ttl_cons_turm = Label(frame_cons_turm, text='Consulta de Turmas', font='System 20 bold', fg='goldenrod', bg='gray15')
ttl_cons_turm.pack()
ent_cons_cod_turm = Entry(frame_cons_turm, font='System 15', fg='gray10', bg='gray70', width='18')
ent_cons_cod_turm.place(x=280, y=60)
txt_cons_turm = Label(frame_cons_turm, text='Código:', font='System 15', fg='goldenrod', bg='gray15')
txt_cons_turm.place(x=220, y=60)
txt_cons_turm1 = Label(frame_cons_turm, text='', font='System 15', fg='goldenrod', bg='gray15')
txt_cons_turm1.place(x=260, y=365)
txt_cons_turm2 = Label(frame_cons_turm, text='', font='System 15', fg='red', bg='gray15')
txt_cons_turm2.place(x=235, y=363)
lista_cons_turm = Listbox(frame_cons_turm,selectbackground= 'gray15', font='System 15', width='65', height='15',
                                            bg='gray70', fg='gray10')
lista_cons_turm.place(x=60, y=100)
bt_cons_turm = Button(frame_cons_turm, text='Consultar', font='System 15', fg='goldenrod', bg='gray25',
                      command=cons_turm)
bt_cons_turm.place(x=250, y=400)
bt_volta_turm = Button(frame_cons_turm, text='Voltar', font='System 15', fg='goldenrod', bg='gray25',
                       command=vlt_cons_turm)
bt_volta_turm.place(x=350, y=400)


# Frame atualizar turmas
frame_att_turm = Frame(janela, bg='gray15', width='640', height='480')
frame_att_turm.propagate(0)
frame_att_turm.place(x=10000, y=0)
ttl_att_turm = Label(frame_att_turm, text='Atualização de Turmas', font='System 20 bold', fg='goldenrod', bg='gray15')
ttl_att_turm.pack()
ent_att_cod_turm = Entry(frame_att_turm, font='System 15', fg='gray10', bg='gray70', width='30')
ent_att_cod_turm.place(x=220, y=100)
check_att_turm = Label(frame_att_turm, text='', font='System 15', fg='limegreen', bg='gray15')
check_att_turm.place(x=550, y=100)
nome_att_turm = Label(frame_att_turm, text='Código da turma:', font='System 15', fg='goldenrod', bg='gray15')
nome_att_turm.place(x=65, y=100)
novo_cod_att_turm = Label(frame_att_turm, text='Novo código da turma:', font='System 15', fg='goldenrod', bg='gray15')
novo_cod_att_turm.place(x=65, y=140)
cod_disc_att_turm = Label(frame_att_turm, text='Código da disciplina:', font='System 15', fg='goldenrod', bg='gray15')
cod_disc_att_turm.place(x=65, y=180)
ent_att_cod_novo_turm = Entry(frame_att_turm, font='System 15',state='disabled', fg='gray10', bg='gray70', width='30')
ent_att_cod_novo_turm.place(x=220, y=140)
per_att_turm = Label(frame_att_turm, text='Período:', font='System 15', fg='goldenrod', bg='gray15')
per_att_turm.place(x=65, y=220)
ent_att_cod_disc_turm = Entry(frame_att_turm, font='System 15', state='disabled', fg='gray10', bg='gray70', width='30')
ent_att_cod_disc_turm.place(x=220, y=220)
ent_att_per_turm = Entry(frame_att_turm, font='System 15', state='disabled', fg='gray10', bg='gray70', width='30')
ent_att_per_turm.place(x=220, y=180)
aviso_att_turm = Label(frame_att_turm, text='⚠', font='System 15', fg='red', bg='gray15')
aviso_att_turm.place(x=165, y=348)
aviso_att_turm1 = Label(frame_att_turm, text='Criar a turma antes de inserir os CPFs', font='System 15', fg='goldenrod', bg='gray15')
aviso_att_turm1.place(x=190, y=350)
bt_att_turm = Button(frame_att_turm, text='Verificar', font='System 10', fg='goldenrod', bg='gray25',
                     command=ver_att_turma)
bt_att_turm.place(x=480, y=95)
bt_att_turm = Button(frame_att_turm, text='Atualizar', font='System 15', fg='goldenrod', bg='gray25',
                     command=att_turma)
bt_att_turm.place(x=200, y=300)
bt_volta_turm = Button(frame_att_turm, text='Voltar', font='System 15', fg='goldenrod', bg='gray25',
                       command=vlt_att_turm)
bt_att_cpf = Button(frame_att_turm, text='Atualizar CPFS', font='System 15', fg='goldenrod', bg='gray25',
                       command=att_cpf)
bt_att_cpf.place(x=284, y=300)
bt_volta_turm.place(x=410, y=300)
# Frame atualizar cpf turma

frame_att_turm_insert = Frame(janela, bg='gray15', width='640', height='480')
frame_att_turm_insert.propagate(0)
frame_att_turm_insert.place(x=10000, y=0)
ttl_att_turm_insert = Label(frame_att_turm_insert, text='Atualizar CPFS', font='System 20 bold', fg='goldenrod', bg='gray15')
ttl_att_turm_insert.pack()
cpf_prof_att_turm = Entry(frame_att_turm_insert, font='System 15', fg='gray10', bg='gray70', width='30')
cpf_prof_att_turm.place(x=220, y=100)
txt_cpf_prof_att_turm = Label(frame_att_turm_insert, text='Professor:', font='System 15', fg='goldenrod', bg='gray15')
txt_cpf_prof_att_turm.place(x=75, y=100)
lista_att_turm_prof = Listbox(frame_att_turm_insert, selectbackground='gray15',  font='System 15', fg='gray10', bg='gray70', width='30', height='10')
lista_att_turm_prof.place(x=60,y=240)
lista_att_turm_alun = Listbox(frame_att_turm_insert, selectbackground='gray15',  font='System 15', fg='gray10', bg='gray70', width='30', height='10')
lista_att_turm_alun.place(x=350,y=240)
cpf_alun_att_turm = Entry(frame_att_turm_insert, font='System 15', fg='gray10', bg='gray70', width='30')
cpf_alun_att_turm.place(x=220, y=140)
aviso_turm_att_insert = Label(frame_att_turm_insert, text='⚠', font='System 15', fg='red', bg='gray15')
aviso_turm_att_insert.place(x=110, y=58)
aviso_turm_att_insert1 = Label(frame_att_turm_insert, text='Clique em cima do CPF que você deseja atualizar', font='System 15', fg='goldenrod', bg='gray15')
aviso_turm_att_insert1.place(x=140, y=60)
aviso_turm_att_insert2 = Label(frame_att_turm_insert, text='| Alunos |', font='System 15 underline', fg='orange', bg='gray15')
aviso_turm_att_insert2.place(x=440, y=210)
aviso_turm_att_insert3 = Label(frame_att_turm_insert, text='| Professores |', font='System 15 underline', fg='orange', bg='gray15')
aviso_turm_att_insert3.place(x=130, y=210)
txt_cpf_alun_att_turm = Label(frame_att_turm_insert, text='Aluno:', font='System 15', fg='goldenrod', bg='gray15')
txt_cpf_alun_att_turm.place(x=75, y=140)
bt_att_prof = Button(frame_att_turm_insert, text='Att prof', font='System 15', fg='goldenrod', bg='gray25',
                       command=att_cpf_prof)
bt_slt_prof = Button(frame_att_turm_insert, text='Selecionar professor', font='System 15', fg='goldenrod', bg='gray25',
                       command=slt_cpf_prof)
bt_att_alun = Button(frame_att_turm_insert, text='Att aluno', font='System 15', fg='goldenrod', bg='gray25',
                       command=att_cpf_aluno)
bt_slt_alun = Button(frame_att_turm_insert, text='Selecionar aluno', font='System 15', fg='goldenrod', bg='gray25',
                       command=slt_cpf_aluno)
bt_volta_turm = Button(frame_att_turm_insert, text='Voltar', font='System 15', fg='goldenrod', bg='gray25',
                       command=vlt_att_cpf_turm)
bt_att_prof.place(x=480, y=95)
bt_att_alun.place(x=480, y=135)
bt_slt_alun.place(x=410, y=180)
bt_slt_prof.place(x=110, y=180)
bt_volta_turm.place(x=300, y=430)

# Frame remover turmas
frame_rem_turm = Frame(janela, bg='gray15', width='640', height='480')
frame_rem_turm.propagate(0)
frame_rem_turm.place(x=10000, y=0)
ttl_rem_turm = Label(frame_rem_turm, text='Remoção de Turma', font='System 20 bold', fg='goldenrod', bg='gray15')
ttl_rem_turm.pack()
esp = Label(frame_rem_turm, text='', font='System 15 bold', fg='gray70', bg='gray15')
esp.pack()
txt_rem_turm = Label(frame_rem_turm, text='Informe o Código da turma que você deseja excluir:', font='System 15 bold',
                     fg='gray70', bg='gray15')
txt_rem_turm.pack()
txt_rem_turm1 = Label(frame_rem_turm, text='Código:', font='System 15 bold', fg='goldenrod', bg='gray15')
txt_rem_turm1.place(x=150, y=90)
ent_rem_turm = Entry(frame_rem_turm, font='System 15', fg='gray10', bg='gray70')
ent_rem_turm.place(x=220, y=90)
bt_rem_turm = Button(frame_rem_turm, text='Deletar', font='System 15', fg='goldenrod', bg='gray25', command=rem_turm)
bt_rem_turm.place(x=300, y=300)
bt_volta_turm = Button(frame_rem_turm, text='Voltar', font='System 15', fg='goldenrod', bg='gray25',
                       command=vlt_rem_turm)
bt_volta_turm.place(x=380, y=300)

# Frame ata turmas
frame_ata_turm = Frame(janela, bg='gray15', width='640', height='480')
frame_ata_turm.propagate(0)
frame_ata_turm.place(x=10000,y=0)
ttl_ata_turm = Label(frame_ata_turm, text='Ata para Turmas', font='System 20 bold', fg='goldenrod',
                 bg='gray15')
ttl_ata_turm.pack(side='top')
txt_ata_turm_cod = Label(frame_ata_turm, text='Código: ', font='System 15', fg='goldenrod', bg='gray15')
txt_ata_turm_cod.place(x=220, y=60)
ent_ata_turm_cod = Entry(frame_ata_turm, font='System 15', fg='gray10', bg='gray70')
ent_ata_turm_cod.place(x=280, y=60)
lista_ata_turm = Listbox(frame_ata_turm,selectbackground= 'gray15', font='System 15', fg='gray10', bg='gray70', width='65', height='15')
lista_ata_turm.place(x=60,y=100)
txt_ata_turm1 = Label(frame_ata_turm, text='', font='System 15', fg='goldenrod', bg='gray15')
txt_ata_turm1.place(x=260, y=365)
txt_ata_turm2 = Label(frame_ata_turm, text='', font='System 15', fg='red', bg='gray15')
txt_ata_turm2.place(x=235, y=363)
bt_ata_turm = Button(frame_ata_turm, text='Gerar', font='System 15', fg='goldenrod', bg='gray25', command=ata_turm)
bt_ata_turm.place(x=250, y=400)
bt_volta_turm = Button(frame_ata_turm, text='Voltar', font='System 15', fg='goldenrod', bg='gray25', command=vlt_ata_turm)
bt_volta_turm.place(x=350, y=400)

janela.mainloop()
