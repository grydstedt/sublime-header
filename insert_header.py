import datetime, getpass, os
import sublime, sublime_plugin

class InsertHeaderCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    author = self.view.settings().get('author_name') or getpass.getuser().lower() or 'No author name'
    project = self.view.settings().get('project_name', '')
    company = self.view.settings().get('company_name')

    header = ('// %s\n'
            '// %s\n'
            '//\n'
            '// Created by %s on %s.\n'
            '// Copyright (c) %s %s. All rights reserved.\n'
            '\n'
            ) % (
            os.path.basename(self.view.file_name() or 'Untitled'), 
            project, 
            author,
            datetime.datetime.now().strftime("%Y/%m/%d"),
            datetime.datetime.now().strftime("%Y"), 
            company
            )

    self.view.insert(edit, 0, header)
