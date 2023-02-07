from django.shortcuts import render
from django.views.generic import TemplateView
from .core import Maze
from pprint import pprint

class TrappedMouseHomeView(TemplateView):
    template_name = 'trapped_mouse/home.html'

    def get(self, request, *args, **kwargs):
        print(request.GET)
        kwargs.update({'row': request.GET.get('row'), 'column': request.GET.get('column')})

        return super().get(request, *args, **kwargs)


    def get_context_data(self,  **kwargs):

        if kwargs.get('row') and kwargs.get('column'):

            line_size = int(kwargs.get('row'))
            column_size = int(kwargs.get('column'))

            maze = Maze(line_size, line_size)

            run = maze.run()

            end_position = []
            for er, r in enumerate(maze.history_maze[-1]):
                end_position.append([])
                for ec, c in enumerate(r):
                    if c == 'm':
                        end_position[er].append('.')
                        continue
                    if c == 'e':
                        end_position[er].append('m')
                        continue

                    end_position[er].append(c)

            maze.history_maze.append(end_position)

            kwargs.update({
                "has_maze": True,
                'result': run,
                'line_size': line_size,
                'column_size': column_size,
                'history_stack': maze.history_stack,
                'history_maze': maze.history_maze
                })

        return super().get_context_data(**kwargs)

trapped_mouse_home = TrappedMouseHomeView.as_view()
