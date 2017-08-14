function valid_email(email){
    return !/^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,5}$/.test(email)
}

function valid_password(password){
	var pattern = /^(?!\D+$)(?![^a-zA-Z]+$).{6,20}$/
	return !pattern.test(password)
}

module.exports = {
    valid_email: valid_email,
    valid_password: valid_password
}
