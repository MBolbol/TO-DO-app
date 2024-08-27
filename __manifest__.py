{
    'name': 'To-Do_Management_List_App',
    'author':'Mostafa Bolbol',
    'version':'1.0',
    'summary':'ToDO management application',
    'depends':['base', 'mail'],
    'data':[
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/todo_task_view.xml',
        'views/users_view.xml'
            
            ],
    'application': True, 
    'license': 'LGPL-3',
   
}