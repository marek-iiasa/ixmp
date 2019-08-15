from abc import ABC, abstractmethod


class Backend(ABC):
    """Abstract base class for backends."""

    def __init__(self):
        """Initialize the backend."""
        pass

    @abstractmethod
    def set_log_level(self, level):
        """Set logging level for the backend and other code (required)."""
        pass

    def open_db(self):
        """(Re-)open a database connection (optional).

        A backend MAY connect to a database server. This method opens the
        database connection if it is closed.
        """
        pass

    def close_db(self):
        """Close a database connection (optional).

        Close a database connection if it is open.
        """
        pass

    @abstractmethod
    def units(self):
        """Return all registered units of measurement (required).

        Returns
        -------
        list of str
        """
        pass

    @abstractmethod
    def ts_init(self, ts, annotation=None):
        """Initialize the TimeSeries *ts* (required).

        The method MAY:

        - Modify the version attr of the returned object.
        """
        pass

    @abstractmethod
    def ts_check_out(self, ts, timeseries_only):
        """Check out the TimeSeries *s* for modifications (required).

        Parameters
        ----------
        timeseries_only : bool
            ???
        """
        pass

    @abstractmethod
    def ts_commit(self, ts, comment):
        """Commit changes to the TimeSeries *s*  (required).

        The method MAY:

        - Modify the version attr of *ts*.
        """
        pass

    @abstractmethod
    def s_init(self, s, annotation=None):
        """Initialize the Scenario *s* (required).

        The method MAY:

        - Modify the version attr of the returned object.
        """
        pass

    @abstractmethod
    def s_has_solution(self, s):
        """Return :obj:`True` if Scenario *s* has been solved (required).

        If :obj:`True`, model solution data is available from the Backend.
        """
        pass

    @abstractmethod
    def s_list_items(self, s, type):
        """Return a list of items of *type* in Scenario *s* (required)."""
        pass

    @abstractmethod
    def s_init_item(self, s, type, name):
        """Initialize an item *name* of *type* in Scenario *s* (required)."""
        pass

    @abstractmethod
    def s_item_index(self, s, name, sets_or_names):
        """Return the index sets or names of item *name* (required).

        Parameters
        ----------
        sets_or_names : 'sets' or 'names'
        """
        pass

    @abstractmethod
    def s_item_elements(self, s, type, name, filters=None, has_value=False,
                        has_level=False):
        """Return elements of item *name* in Scenario *s* (required).

        The return type varies according to the *type* and contents:

        - Scalars vs. parameters.
        - Lists, e.g. set elements.
        - Mapping sets.
        - Multi-dimensional parameters, equations, or variables.
        """
        # TODO exactly specify the return types in the docstring using MUST,
        # MAY, etc. terms
        pass

    @abstractmethod
    def s_add_set_elements(self, s, name, elements):
        """Add elements to set *name* in Scenario *s* (required).

        Parameters
        ----------
        elements : iterable of 2-tuples
            The tuple members are, respectively:

            1. Key: str or list of str. The number and order of key dimensions
               must match the index of *name*, if any.
            2. Comment: str or None. An optional description of the key.

        Raises
        ------
        ValueError
            If *elements* contain invalid values, e.g. for an indexed set,
            values not in the index set(s).
        Exception
            If the Backend encounters any error adding the key.
        """
        pass

    @abstractmethod
    def s_add_par_values(self, s, name, elements):
        """Add values to parameter *name* in Scenario *s* (required).

        Parameters
        ----------
        elements : iterable of 4-tuples
            The tuple members are, respectively:

            1. Key: str or list of str or (for a scalar, or 0-dimensional
               parameter) None.
            2. Value: float.
            3. Unit: str or None.
            4. Comment: str or None.

        Raises
        ------
        ValueError
            If *elements* contain invalid values, e.g. key values not in the
            index set(s).
        Exception
            If the Backend encounters any error adding the parameter values.
        """
        pass
