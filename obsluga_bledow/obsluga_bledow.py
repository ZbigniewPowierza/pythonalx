lista = [1, 0, 10, 'a']

# for i in lista:
#     try:
#         print(10/i)
#     except ZeroDivisionError:
#         print("Dzielisz przez zero")
#     except TypeError:
#         print("Dzielisz prze 'nie-liczbę'")
#     except Exception:
#         pass
#     finally:
#         print("wykonałem sie")

lista = [1, 0, 10, 'a']
for i in lista:
    try:
        print(10/i)
    # except ZeroDivisionError:
    #     print("Dzielisz przez zero")
    except TypeError:
        print("Dzielisz przez 'nie-liczbę'")
    except Exception:
        pass
    finally:
        print("wykonałem sie")