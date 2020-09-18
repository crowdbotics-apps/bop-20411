import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import ArticleList103615Navigator from '../features/ArticleList103615/navigator';
import ArticleList103614Navigator from '../features/ArticleList103614/navigator';
import ArticleList103613Navigator from '../features/ArticleList103613/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
ArticleList103615: { screen: ArticleList103615Navigator },
ArticleList103614: { screen: ArticleList103614Navigator },
ArticleList103613: { screen: ArticleList103613Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
