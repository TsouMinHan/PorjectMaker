let data = {
    projectId: null,
    projectName: "",
    projectOptions: [],
    projectPackage: [],
    projrctSelectedPackageIndex: [],
    msg: "",
}

let vm = new Vue({
    el: "#app",
    data: data,
    mounted: async function () {
        data.projectOptions = await eel.get_project_options()();
        const tempJson = await eel.get_project_package()();
        for (var i in tempJson){
            data.projectPackage.push(tempJson[i]);
        }
    },
    methods: {
        createProject: async function(projectName, projectId) {
            if (projectName && projectId!=null){
                const copyPath = data.projectOptions[projectId].path;
                const projectPackage = {};
                data.projrctSelectedPackageIndex.forEach(index => {
                    projectPackage[data.projectPackage[index].name] = data.projectPackage[index].command;
                });
                c(projectPackage)
                result = await eel.create_project(copyPath, projectName, projectPackage)();
                data.msg = result;

                return
            }
            data.msg = "請輸入名稱與選項";
        },
        showWindow: async function(name) {
            await eel.show_window(name)();
        }
    }

})

function c(obj) {
    console.log(obj);
}
