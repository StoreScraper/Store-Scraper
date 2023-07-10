package Models
import kotlinx.serialization.Serializable
@Serializable
data class BasicUser(val id: Int, val username: String, val email: String, val password: String)