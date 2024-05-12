-- Active: 1714724041901@@127.0.0.1@3306@lr2
<template>
    <div class="list">
        <ul class="list_content" v-for="item in this.log">
            <li v-for="el in item">
                <div class="main">
                    <div>
                        <p>{{ el.id }}</p>
                    </div>
                    <div><textarea cols="100">{{ el.data }}</textarea></div>
                </div>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            log: [],
        };
    },
    methods: {
    },
    computed: {

    },

    created() {
        axios.defaults.headers.common['Authorization'] = "Token " + localStorage.getItem('token')
        axios.get('http://localhost:8003/log/')
            .then((response) => {
                this.log = Object.values(response.data);
            })
            .catch(err => console.log(err))
    },

}
</script>

<style lang="scss" scoped>

* {
    font-family: 'Roboto', sans-serif;
}

.list li {
    border: 2px solid rgb(51, 182, 123);
    border-radius: 5px;
    margin-bottom: 10px;
    padding: 10px;
    background-color: #0c0c0c;
}

.search {
    background-color: #0c0c0c;
}

#date {
    background-color: #0c0c0c;
    color: #ffffff;
}

#search {
    padding-bottom: 10px;
    width: calc(100% - 22%);
    margin: 0 auto;
    display: flex;
    justify-content: space-around;

}

#search>div {
    width: 100%;
}

#search>div:first-child {
    margin-right: 10px;
}

input {

    margin: 0 auto;
    border: 2px solid rgb(51, 182, 123);
    background-color: #0c0c0c;

}

.list_content {
    width: calc(100% - 22%);
    margin: 0 auto;
    list-style: none;
    padding: 0;
}

.list {
    background-color: #0c0c0c;
}

.main {
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    align-items: center;
    border-radius: 5px;
}

p {
    color: #ffffff;
    margin-bottom: 0%;

}

textarea {
    width: calc(100%);
    border: #ffffff;
    background-color: #0c0c0c;
    color: #ffffff;
}

@media (max-width: 600px) {
    #search {
        display: block;
    }

    #search>div {
        margin-bottom: 10px;
    }
}


@media (max-width: 1200px) {
    .main {
        display: block;
    }



    .main>div {
        text-align: center;
    }

}
</style>
