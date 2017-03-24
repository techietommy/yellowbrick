# tests.test_cluster.test_elbow
# Tests for the KElbowVisualizer
#
# Author:   Benjamin Bengfort <bbengfort@districtdatalabs.com>
# Created:  Thu Mar 23 22:30:19 2017 -0400
#
# Copyright (C) 2016 District Data Labs
# For license information, see LICENSE.txt
#
# ID: test_elbow.py [] benjamin@bengfort.com $

"""
Tests for the KElbowVisualizer
"""

##########################################################################
## Imports
##########################################################################

from ..base import VisualTestCase
from ..dataset import DatasetMixin

from sklearn.cluster import KMeans
from yellowbrick.cluster.elbow import KElbowVisualizer
from yellowbrick.exceptions import YellowbrickValueError


##########################################################################
## KElbowVisualizer Test Cases
##########################################################################

class KElbowVisualizerTests(VisualTestCase, DatasetMixin):

    def test_integrated_elbow(self):
        """
        Test that no errors occur on k-elbow on real dataset
        """

        try:
            # Load the data from the fixture
            data = self.load_data('occupancy')
            X = data[[
                "temperature", "relative_humidity", "light", "C02", "humidity"
            ]]

            # Convert X to an ndarray
            X = X.view((float, len(X.dtype.names)))

            visualizer = KElbowVisualizer(KMeans(), k=4)
            visualizer.fit(X)
            visualizer.poof()

        except Exception as e:
            self.fail("error during k-elbow: {}".format(e))

    def test_invalid_k(self):
        """
        Assert that invalid values of K raise exceptions
        """

        with self.assertRaises(YellowbrickValueError):
            model = KElbowVisualizer(KMeans(), k=(1,2,3,4,5))

        with self.assertRaises(YellowbrickValueError):
            model = KElbowVisualizer(KMeans(), k="foo")
