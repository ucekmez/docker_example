import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

const APIURL = "http://localhost:7778";

class App extends Component {
  state = {
    news:  [],
  };

  componentDidMount(prevProps) {
    const _this = this;
    axios.get(APIURL)
      .then(function (response) {
        _this.setState({news: response.data.articles})
        console.log(response.data);
      })
      .catch(function (error) {
        console.log(error);
      });
  }


  saveRecord = (data) => {
    axios.post(APIURL+'/save', data)
      .then(function (response) { console.log("OK"); })
      .catch(function (error) { console.log(data); });
  }


  render() {
    const _this = this;
    return (
      <div className="App">
        <h1 className="App-title">Sıcak haberler</h1>
        <hr />
        {this.state.news.length > 0 ? this.state.news.map(function(data, index){
          return <label key={index}>
            <h3>{data.title}</h3>
            <a href={data.url}><img style={{maxHeight:100}} src={data.urlToImage} /></a>
            <br />
            <label>{data.description}</label>
            <br />
            <button onClick={_this.saveRecord.bind(this, data)}>KAYDET</button>
            <hr />
          </label>
        }) : "Yükleniyor ..."}
      </div>
    );
  }
}

export default App;
