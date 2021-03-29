import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class JavaPrepareStatement {
    public static void main(String[] args) throws SQLException {
        int userId = 1;
        Connection connection = null;

        String sql = "SELECT * FROM Users WHERE UserId = ?";
        PreparedStatement statement = connection.prepareStatement(sql);
        statement.setInt(1, userId);
        ResultSet results = statement.executeQuery();
    }

}
