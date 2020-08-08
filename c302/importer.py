def dynamic_import(abs_module_path, class_name):

    from importlib import import_module

    module_object = import_module(abs_module_path)

    target_class = getattr(module_object, class_name)

    return target_class
