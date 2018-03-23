These instructions are for configuring a production server for Agrifood on Alpine Linux.

This guide will assume that all of the relevant folders/files will reside in the directory: `/srv/agrifood-project` but you can follow the instructions for any directory. Just switch `/srv/agrifood-project` in the instructions with your own project directory.

Run the following commands in your Alpine terminal:
```
// Update packages and add git
apk update
apk upgrade
apk add git

// Clone the backend directory and run the init-agrifood script that will set up MongoDB and Solr
mkdir -p /srv/agrifood-project
cd /srv/agrifood-project
git clone https://github.com/UBC-LFS/lfs-agrifood-backend.git
cd /srv/agrifood-project/lfs-agrifood-backend
chmod +x init-agrifood.sh
./init-agrifood.sh

// Clone the frontend directory and run the init-cms script that will set up Node
cd /srv/agrifood-project
git clone https://github.com/UBC-LFS/lfs-agrifood-cms.git
cd /srv/agrifood-project/lfs-agrifood-cms
chmod +x init-cms.sh
./init-cms.sh
```

At this point, Solr should be available at port 8983, and the Node app should be available at port 3000.
