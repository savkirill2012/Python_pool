import yaml

with open("../../materials/todo.yml") as yf:
    data = yaml.load(yf, Loader=yaml.FullLoader)

new_file = {"config": {}}

new_file["config"] = {"ansible.builtin.apt": {"name": [], "state": "latest"}}

for elem in data["server"]["install_packages"]:
    new_file["config"]["ansible.builtin.apt"]["name"].append(elem)

new_file["config"] |= {"ansible.builtin.copy": {"src": [], "dist": []}}

for file in data["server"]["exploit_files"]:
    new_file["config"]["ansible.builtin.copy"]["src"].append(f"./{file}")
    new_file["config"]["ansible.builtin.copy"]["dist"].append(f"/path/{file}")

new_file["config"] |= {"ansible.builtin.shell": {"cmd": []}}

for file in data["server"]["exploit_files"]:
    if file == 'exploit.py':
        new_file["config"]["ansible.builtin.shell"]["cmd"].append(
            f"python3 {file}"
        )
    else:
        new_file["config"]["ansible.builtin.shell"]["cmd"].append(
            f"python3 {file} -e {','.join(data['bad_guys'])}"
        )

with open("deploy.yml", "w") as nf:
    nf.write(yaml.dump(new_file))
