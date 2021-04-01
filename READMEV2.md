# Assignment 1

Program is written to get the vendor details using the API key and MACaddress.

This code is taking the MACaddress and apikey from the user. 
Both are used to access as specific client to URL: https://macaddress.io 
to get vendor details from the website.

On CLI user has to provide:  
**`python FetchCompanyDetails -m MACaddress -a apikey`**

For example:  
 `python FetchCompanyDetails -m 45:48:39:fe:ff:56 -a at_SoUgEBdgXBpyWK258Ix0tKBwL`
 
Output example:  
**Device vendor is Cumulus Networks, Inc**
