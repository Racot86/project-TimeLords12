from bot.src.tools.StorageController import StorageController
from bot.src.classes.class_Note import Note
from bot.src.classes.class_NoteBook import NoteBook
from prompt_toolkit import prompt
from bot.src.tools.a_print import a_print
from bot.settings import Settings


def print_list(match, search_criteria):
    if len(match) > 0:
        a_print('This is what I found for ' + ' '.join(search_criteria), main_color=Settings.msg_color,
                prefix=Settings.TARDIS)
        for itm in match:
            if match[itm] != []:
                a_print(f"  {Settings.msg_color}{itm}{Settings.shadow_color} present in {Settings.end_all + Settings.msg_color}<{'> <'.join(match[itm])}>{Settings.shadow_color} note(s){Settings.end_all}",
                        used_colors=[Settings.msg_color,Settings.shadow_color,Settings.end_all])
            else:
                a_print(f"  '{itm}' not found at the current time flow", main_color=Settings.shadow_color + Settings.msg_color)
    else:
        a_print(f'Sir, there are no matches for your request', prefix='TARDIS: ', main_color=Settings.warning_color)


def n_filter_cmd(cmd):
    if len(cmd) > 3 and cmd[1].lower() == 'by' and cmd[2].lower() == 'tag':
        storage = StorageController()
        notes = storage.load_note_book()
        cmd.pop(0)
        cmd.pop(0)
        cmd.pop(0)
        validated_list = []
        for itm in cmd:
            if itm[0] == '#' and len(itm) > 1:
                validated_list.append(itm)
        if len(validated_list) > 0:
            sorted_dict = {}
            for itm in validated_list:
                for note in notes:
                    for tag in note.tags:
                        if tag.lower() == itm.lower():
                            sorted_dict[itm] = []
            for tag in sorted_dict:
                for note in notes:
                    if tag in note.tags:
                        if note.title not in sorted_dict[tag]:
                            sorted_dict[tag].append(note.title)

            print_list(sorted_dict, validated_list)

        else:
            a_print(f'Check you input data.For your information tags are starting with # character must be at least two characters long',
                    prefix='TARDIS: ',
                    main_color=Settings.warning_color
                    )

    else:
        a_print(f'Doctor, are you Ok? Check what you are typing!',
                prefix='TARDIS: ',
                main_color=Settings.warning_color
                )
