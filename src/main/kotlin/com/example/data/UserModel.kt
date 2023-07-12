package com.example.data

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class User(
    val userId: Int = 0,
    val email: String = "",
    val userCreateDate: String = "",
)