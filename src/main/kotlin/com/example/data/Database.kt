package com.example.data
import kotlinx.coroutines.*
import org.jetbrains.exposed.sql.*
import org.jetbrains.exposed.sql.transactions.*
import org.jetbrains.exposed.sql.transactions.experimental.*

object DatabaseFactory {
    fun init(): Database {
        val driverClassName = "org.postgresql.Driver"
        val jdbcURL = "jdbc:postgresql://localhost:5432"
        return Database.connect(jdbcURL, driverClassName, user = "isaac", password = "coolPassword")
    }
}