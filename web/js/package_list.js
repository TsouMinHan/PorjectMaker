let data = {
    projectPackage: [],
    insertObj: {
        "name": null,
        "command": null,
        "targets": null,
    },
    msg: "",
}

let vm = new Vue({
    el: "#app",
    data: data,
    mounted: async function () {
        this.setProjectPackage();
    },
    methods: {
        setProjectPackage: async function (){
            data.projectPackage = [];
            const tempJson = await eel.get_project_package()();
            for (var i in tempJson) {
                data.projectPackage.push(tempJson[i]);
            }
            data.msg = "";
        },
        insert: async function (obj) {

            if (!obj.name || !obj.command || !obj.targets) {
                data.msg = "請輸入名稱、指令、以及對象";
                return
            }

            await eel.insert_to_package_list(obj);
            this.setProjectPackage();
            data.insertObj = {
                "name": null,
                "command": null,
                "targets": null,
            }

        },
        deleteData: async function (id) {
            await eel.delete_from_package_list(String(id))();
            this.setProjectPackage();
            c(typeof(id))
        },
        modify: async function(id, obj) {
            const name = obj.name;
            const command = obj.command;
            const targets = obj.targets;
            if (!name || !command || !targets) {
                data.msg = "請輸入修改名稱、指令、以及對象";
                return
            }

            eel.modify_package_list(String(id), obj)();
            data.msg = "修改完成";
        }
    }

})

function c(obj) {
    console.log(obj);
}
