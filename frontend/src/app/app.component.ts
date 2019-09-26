import { Component, OnInit } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import { DomSanitizer} from '@angular/platform-browser';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent  implements OnInit {
  title = 'frontend';
  backend_url = 'http://127.0.0.1:5001/api/get_dashboard';
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  };

  urlToEmbed;

  constructor(private http: HttpClient,
              private sanitizer: DomSanitizer) {
  }

  ngOnInit() {
    this.http.get(this.backend_url, this.httpOptions).subscribe((r: any)=> {
      console.log(r);

      this.urlToEmbed = r.embeddedUrl;
    }, (err) => {
      console.log(err);
    });
  }

  getUrl() {
    return this.sanitizer.bypassSecurityTrustResourceUrl(this.urlToEmbed);
  }
}
