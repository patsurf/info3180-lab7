<template>
    <form @submit.prevent="uploadPhoto" id="uploadForm" method="POST" enctype="multipart/form-data">
        <div v-if="message" class="alert alert-success" role="alert">{{ message }}</div>
        <li v-for ="err in errorFlask " class="alert alert-danger" role="alert">{{ err }}</li>

        <div class="form-group">
            <label for="photo" id="photo-Label">Photo Upload</label>
            <div></div>
            <input
                type="file"
                class="form-control-file"
                id="photo"
                name="photo"
                @change="fileSelected"
            />
        </div>
        <div class="form-group">
            <label for="description">Description</label>
            <textarea class="form-control" id="description" name="description" rows="3"></textarea>
        </div>
        <div></div>
        <button type="submit" class="btn btn-primary">Upload</button>
    </form>
</template>


<script>
export default {
    data() {
        // having issues here
        return { csrfToken: '', message: '', errorFlask: [] }
    },
    created() {
        this.getCsfrToken();
    },
    methods: {
        uploadPhoto() {
            let uploadForm = document.getElementById('uploadForm');
            let form_data = new FormData(uploadForm);
            let self = this;
            fetch("/api/upload", {
                method: 'POST',
                body: form_data,
                headers: {
                    'X-CSRF-TOKEN': this.csrfToken
                }
            })
                .then(function (response) {
                    return response.json();
                })
                .then(function (data) {
                    // display a success message
                    self.message = data.message;
                    console.log(data);
                    if(data.errors.length > 0) {
                        self.errorFlask = data.errors;
                    }
                })
                .catch(function (error) {
                    // display an error message
                    // Having issues here
                    self.errorFlask = error.errors;
                    console.log(error);
                });
        },
        getCsfrToken() {
            let self = this;
            fetch("/api/csrf-token")
                .then((response) => {
                    return response.json();
                })
                .then((data) => {
                    console.log(data);
                    self.csrfToken = data.csrf_token;
                })
        }
    },
};
</script>

<style>
.form-group {
    margin-bottom: 15px;
}
#photo-Label {
    margin-top: 15px;
    margin-bottom: 5px;
}
</style>
