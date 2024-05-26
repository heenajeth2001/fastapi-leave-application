 function Main() {
    return {
        currentID:null,
        startDate: "",
        endDate: "",
        reason: "",
        isAdd: true,
        isApproved: true,
        // Modals
        isLeaveModalOpen: false,
        isApprovedModal: false,
        isRejectModalOpen: false,
        isDeleteModalOpen: false,
        currentItem : null,
        openLeaveModal() {
            this.isLeaveModalOpen = true;
            this.isAdd = true;
        },
        closeLeaveModal() {
            this.isLeaveModalOpen = false;
            this.startDate = "";
            this.endDate = "";
            this.reason = "";
        },
        openApproveRejectModal(item,status){
            this.isApprovedModal = true;
            this.currentItem = item;
            status == 1 ? this.isApproved = true : this.isApproved = false;
        },
        closeApproveModal(){
            this.isApprovedModal = false;
            this.currentItem = null;
        },
        approveRejectHandler(status) {
            let item = this.currentItem;
            console.log(item.id);
            let updateItem = this.items.filter(t=>t.id==item.id)[0];
            this.items = this.items.filter(t=>t.id!=item.id);
            status == 1 ? updateItem.status = 'Approved' : updateItem.status = 'Rejected';
            this.items.push(updateItem);
            this.items.sort((a, b) => a.id - b.id);
            this.currentItem = null;
            this.isApprovedModal = false;
        },
        items: [
            {
                id : 1,
                startDate : '05-08-2023',
                endDate : '06-12-2023',
                reason : 'Birthday',
                status : 'Pending'
            },
            {
                id : 2,
                startDate : '06-08-2023',
                endDate : '10-12-2023',
                reason : 'Birthday',
                status : 'Pending'
            },
            {
                id : 3,
                startDate : '12-08-2023',
                endDate : '20-12-2023',
                reason : 'Birthday',
                status : 'Pending'
            }
        ],
        statusClass(status) {
            if (status === 'pending') {

            } else if (status === 'Approved') {
                
            } else if (status === 'Rejected') {

            }

            return '';
        },
        addData() {
           
            if (this.isAdd){
                const newItem = {
                    id: this.items.length + 1,
                    startDate: this.startDate,
                    // startDate: new Date(this.startDate).toLocaleDateString('en-GB').replaceAll('/','-'),
                    endDate: this.endDate,
                    // endDate: new Date(this.endDate).toLocaleDateString('en-GB').replaceAll('/','-'),
                    reason: this.reason,
                    status: 'Pending'
                };
                
                if(this.startDate <= this.endDate){

                    this.items.push(newItem);
                }
                else{
                    alert('Please Enter Valid Start Date and End Date.');
                    return false;
                }
                
            }
            else{
                let updateItem = this.items.filter(t=>t.id==this.currentID)[0];
                this.items = this.items.filter(t=>t.id!=this.currentID)
                updateItem.startDate = this.startDate;
                updateItem.endDate = this.endDate;
                updateItem.reason = this.reason;
                this.items.push(updateItem);
            }
           
            this.items.sort((a, b) => a.id - b.id);
            this.isLeaveModalOpen = false;
            this.startDate = "";
            this.endDate = "";
            this.reason = "";
        },
        changeStatus(item, newStatus) {
            item.status = newStatus;
        },
        deleteData(item) {
            console.log(item.id);
            this.isDeleteModalOpen = true;
            this.items.splice(this.items.indexOf(item), 1);
            console.log('Data is being Deleted');
            
        },
        editData(item) { 
            this.currentID = item.id;
            if(item.status == "Approved"){
                this.isLeaveModalOpen=false;
                alert("Sorry, You can't Modify your Data!")
                return false;

                
            }
            else if(item.status == "Rejected"){
                this.isLeaveModalOpen=false;
                alert("Sorry, You can't Modify your Data!")
                return false;
            }
            else{
                this.isLeaveModalOpen = true;
            }

          
            this.startDate = item.startDate;
            this.endDate = item.endDate;
            this.reason = item.reason;
            this.isAdd = false;
             
        }
    }

}
