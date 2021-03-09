
from settings import DB
import  psycopg2


class DBManager:
    __connection = None
    __cursor = None
    __is_connected=False
    def __init__(self):
        pass

    def commit(self, query, args=()):
        # Use for INSERT UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        self.__connect()
        self.__execute(query, args)
        self.__connection.commit()
        affected_rows = self.__cursor.rowcount
        self.__close_connection()
        return affected_rows

    def fetch(self, query, args=()):
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = False
        self.__connect()
        if self.__execute(query, args):
            query_result = self.__cursor.fetchall()
        self.__close_connection()
        # temp = []
        # for x in query_result:
        #     temp2 = {}
        #     c = 0
        #     for col in self.__cursor.description:
        #         temp2.update({str(col[0]): x[c]})
        #         c = c + 1
        #     temp.append(temp2)
        #
        # return temp
        return query_result
    def execute(self, query, args=()):
        # Use for CREATE, DROP AND ALTER statements.
        self.__connect()
        query_result = self.__execute(query, args)
        self.__close_connection()
        return query_result

    def __connect(self):
        # Opens a connection to the database.
        try:
            DB_HOST = "ec2-52-71-231-37.compute-1.amazonaws.com"
            DB_PORT = "5432"
            DB_USER = "pdunuxlwaesfsn"
            DB_PASSWORD = "c48b2dd83087bb929a1e53d3857460c94d50a6fc292ad224162f1fe3b9203be9"
            DB_NAME = "dap6sst8tt2q2a"


            conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)

            if not self.__connection or not self.__is_connected:
                self.__connection = conn
                self.__cursor = conn.cursor()
                self.__is_connected=True
        except self.__connection.Error as error:
            print("Connection failed with error {}".format(error))

    def __execute(self, query, args=()):
        # Executes a given query with given args, if provided.
        if query:
            try:
                self.__cursor.execute(query, args)
                return True
            except self.__connection.Error as error:
                print("Query failed with error {}".format(error))
        return False

    def __close_connection(self):
        # Closes an open database connection.
        try:
            if not self.__connection or not self.__is_connected:

                self.__connection.close()
                self.__cursor.close()
                self.__is_connected=False
        except self.__connection.Error as error:
            print("Failed to close connection with error {}".format(error))


# Creates an instance for the DBManager class for export.
dbManager = DBManager()