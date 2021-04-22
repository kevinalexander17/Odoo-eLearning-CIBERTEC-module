# -*- coding: utf-8 -*-
{
    'name': "cibertec eLearning",
    'version': '13.0.1.1.2',
    'license': 'LGPL-3',
    'depends': ['base','website'],
    'author': "Kevin Alexander Quispe Roman",
    'category': 'Uncategorized',

    'summary': 'Manage the course development process about a student',

    'description': """
        Cibertec eLearning menu
        - Cibertec menu: First of all, we have three menu items(courses, content and category)
            Menu items:
            - Curso: It allows you to display a kanban view of all the courses that have been registered.
                        Furthermore, there is a button that can change the view from a kanban view to a tree 
                        view just if you want to. Apart from that, we can do a  CRUD operation(create, read, 
                        update and delete) just using buttons that are around in the form view.

            - Contenido: Here, you will be able to display a kanban view of all the contents that the administrator
                         has been registered. Moreover, there is a button that can change the view from a kanban view
                         to a tree view just if you want to. In addition to this, we can do a  CRUD operation(create, 
                         read, update and delete) just using buttons that are around in the form view.
            
            - Categoría: In this point, we can do a CRUD operation(create, read, update and delete) so, these categories 
                        will be shown as a Selection widget when the the user registers a course.

        - Configuration menu: The next stage, we've got two menu items(tags and partners)
            Menu items:
                - Etiqueta: To start with, we can do a CRUD operation(create, read, update and delete) so, these categories 
                        will be shown as a Selection widget when the the user registers a course.

                - Usuario: Besides, Here we inherit from res.partner views so that we can do a CRUD operation. Also, we can
                            select a course we want to take as well as the contents we have done.
    """,

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/course_view.xml',
        'views/tag_view.xml',
        'views/content_view.xml',
        'views/partner.xml',
        'views/category.xml',
        'views/templates.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
