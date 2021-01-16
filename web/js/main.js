let data = {
    projectName: "",
    projectLanguage: "",
    projectOptions: [],
    projectPackage: [
        {"name": "git", "command": "some command", targets: ["Python", "JavaScript"]},
        {"name": "venv", "command": "some command", targets: ["Python"]},
    ]
}

let vm = new Vue({
    el: "#app",
    data: data,
    mounted: async function () {
        data.projectOptions = await eel.get_project_options()();
        c(data.projectOptions)
    },
    methods: {
        
    }

})

function c(obj) {
    console.log(obj);
}
