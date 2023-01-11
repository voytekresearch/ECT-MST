"""plotting functions for ECT"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


###########################################################################
################################ FUNCTIONS ################################
###########################################################################

def plot_feature_prepost(exp_df_mean, feature=''):
    """Creates a plot of a given feature from the dataframe,
       comparing its value before and after treatment

    Parameters
    ----------
    exp_df_mean: pandas DataFrame
        dataframe containing extractec features, averaged across electrodes
    feature: str
        feature of interest; 'alphas', 'thetas', 'chans_exps'

    Returns
    -------
    plot: matplotlib obj
        plot of feature pre/post treatment
    """
    
    pats = np.unique(exp_df_mean['patient'])

    # means of alphas across patient, channels
    means_pre = exp_df_mean[exp_df_mean['pre_post']=='pre'][feature].values
    means_post = exp_df_mean[exp_df_mean['pre_post']=='post'][feature].values

    sns.set_context('poster')

    plt.figure(figsize=(5,8))
    x1, x2 = 0.5, 1.5

    for pat in pats:

        point_pre = exp_df_mean[(exp_df_mean['patient']==pat) &
                                (exp_df_mean['pre_post']=='pre')][feature].values
        point_post = exp_df_mean[(exp_df_mean['patient']==pat) &
                                 (exp_df_mean['pre_post']=='post')][feature].values
        xdat1= x1+np.random.normal(0, 0.025, 1)
        xdat2= x2+np.random.normal(0, 0.025, 1)


        plt.plot([xdat1,xdat2], [point_pre, point_post], color='k', alpha=0.05, lw=5)
        plt.scatter(xdat1, point_pre, color='royalblue', alpha=0.7)
        plt.scatter(xdat2, point_post, color='salmon', alpha=0.7)

    plt.plot([x1-0.2, x1+0.2], [np.nanmean(means_pre), np.nanmean(means_pre)], lw=7, c='royalblue')
    plt.plot([x2-0.2, x2+0.2], [np.nanmean(means_post), np.nanmean(means_post)], lw=7, c='salmon')
            
    plt.xlim([0, 2])

    plt.xticks([x1, x2], ["pre", "post"])

#     if feature == 'alphas':
#         ylabel = 'Alpha Frequency (Hz)'
#     elif feature == 'thetas':
#         ylabel = 'Theta Frequency (Hz)'
#     elif feature == 'chans_exps':
#         ylabel = 'Aperiodic Exponent'
#     else:
#         ylabel = feature[:5]+' power'

#     plt.ylabel(ylabel)

    plt.tight_layout()



def plot_feature_prepost_sessions(exp_df_mean, feature=''):
    """plot feature by pre/post across all 4 sessions

    Parameters
    ----------
    exp_df_mean: pandas DataFrame
        dataframe containing extractec features, averaged across electrodes
    feature: str
        feature of interest; 'alphas', 'thetas', 'chans_exps'

    Returns
    -------
    plot: matplotlib obj
        plot of feature pre/post treatment of all sessions
    """

    pats = np.unique(exp_df_mean['patient'])

    plt.figure(figsize=(15,4))
    x_vals = [1, 2, 3, 4]

    for pat in pats:
        sess = exp_df_mean[exp_df_mean['patient']==pat]['sessions'].unique()
        for ses in sess:
            # get x val for plot
            if ses == 1:
                x1, x2 = x_vals[0]-0.25, x_vals[0]+0.25
            if ses == 4:
                x1, x2 = x_vals[1]-0.25, x_vals[1]+0.25
            if ses == 8:
                x1, x2 = x_vals[2]-0.25, x_vals[2]+0.25
            if ses == 12:
                x1, x2 = x_vals[3]-0.25, x_vals[3]+0.25
            
            # pre/post exponent vals for each session
            point_pre = exp_df_mean[(exp_df_mean['patient']==pat) &
                                    (exp_df_mean['sessions']==ses) &
                                    (exp_df_mean['pre_post']=='Pre')][feature].values
            point_post = exp_df_mean[(exp_df_mean['patient']==pat) &
                                     (exp_df_mean['sessions']==ses) &
                                     (exp_df_mean['pre_post']=='Post')][feature].values
            xdat1= x1+np.random.normal(0, 0.025, 1)
            xdat2= x2+np.random.normal(0, 0.025, 1)

            # skip if pre&post not present
            if point_pre.shape[0]==0 or point_post.shape[0]==0:
                pass
            else:
                plt.plot([xdat1,xdat2], [point_pre, point_post], color='k', alpha=0.05, lw=5)
                plt.scatter(xdat1, point_pre, color='darkmagenta', alpha=0.7)
                plt.scatter(xdat2, point_post, color='forestgreen', alpha=0.7)

    plt.xlim([0.5, 4.5])

    plt.xticks(x_vals, ["1", "4", "8", "12"])

    if feature == 'alphas':
        ylabel = 'Alpha CF'
    if feature == 'alpha_pows':
        ylabel = 'Alpha Power'
    if feature == 'thetas':
        ylabel = 'Theta CF'
    if feature == 'theta_pows':
        ylabel = 'Theta Power'
    if feature == 'chans_exps':
        ylabel = 'Aperiodic Exponent'

    plt.ylabel(ylabel)
    plt.xlabel('Session')

    plt.tight_layout()


def plot_feature_sessions(df, feature='', prepost=''):
    """plot feature over session from pre or post only

    Parameters
    ----------
    df: pandas DataFrame
        dataframe containing pre (or post) only measurements
    feature: str
        feature of interest; alphas, thetas, chans_exps
    prepost: str
        pre or post session recording included in plot; pre, post, diff

    Returns
    -------
    plot: matplotlib obj
        plot of single feature (Y) from pre or post only recording over sessions (X)
        """
    pats = np.unique(df['patient'])
    
    fig, ax = plt.subplots(1,1, figsize=(12,8))
    
    #plt.figure(figsize=(12,8))
    cmap = [plt.cm.tab20b(i) for i in np.linspace(0, 1, len(pats))]  
    ax.set_prop_cycle('color', cmap)  

    x_vals = [1, 4, 8, 12]

    for pat in pats:
        ydat = []
        xdat = []
        sess = df[df['patient']==pat]['sessions'].unique()
        for ses in sess:
            if ses == 1:
                x = x_vals[0]
            if ses == 4:
                x = x_vals[1]
            if ses == 8:
                x = x_vals[2]
            if ses == 12:
                x = x_vals[3]
            # pre/post exponent vals for each session
            point_pre = df[(df['patient']==pat) &
                           (df['sessions']==ses) &
                           (df['pre_post']=='Pre')][feature].values
            point_post = df[(df['patient']==pat) &
                            (df['sessions']==ses) &
                            (df['pre_post']=='Post')][feature].values
            if point_pre.shape[0]==0:# point_post.shape[0]==0:
                pass
            else:
                if prepost == 'diff':
                    diff = point_post-point_pre
                    ydat.append(diff)
                    xdat.append(x)
                if prepost == 'pre':
                    ydat.append(point_pre)
                    xdat.append(x)
                if prepost == 'post':
                    ydat.append(point_post)
                    xdat.append(x)
        ax.plot(xdat, ydat,'o-', alpha=0.9, lw=5)

    ax.set_xlim([x_vals[0]-0.5, x_vals[-1]+0.5])
    #plt.ylim([-5, 5])

    plt.xticks(x_vals, ["1", "4", "8", "12"])

    if feature == 'alphas':
        ylabel = 'Alpha CF'
    elif feature == 'thetas':
        ylabel = 'Theta CF'
    elif feature == 'chans_exps':
        ylabel = 'Aperiodic Exponent'
    else:
        ylabel = feature[:5]+' power'

    if prepost == 'diff':
        ax.set_ylabel('$\Delta$ ' + ylabel)
    else:
        ax.set_ylabel(ylabel)

    ax.set_xlabel('Session')

    plt.tight_layout()


def plot_hemi_feature_prepost(df, feature=''):
    """Creates a plot of a given feature from the dataframe,
       comparing its value in each hemisphere before and after treatment

    Parameters
    ----------
    df: pandas DataFrame
        dataframe containing extractec features, averaged across electrodes
    feature: str
        feature of interest; 'alphas', 'thetas', 'chans_exps'

    Returns
    -------
    plot: matplotlib obj
        plot of feature pre/post treatment
    """
    
    pats = np.unique(df['patient'])

    # means of alphas across patient, sessions, channels, L & R hemispheres
    means_pre_left = df[(df['pre_post']=='Pre') &
                        (df['hemis']=='Left')][feature].values
    means_pre_right = df[(df['pre_post']=='Pre') &
                         (df['hemis']=='Right')][feature].values
    means_post_left = df[(df['pre_post']=='Post') &
                         (df['hemis']=='Left')][feature].values
    means_post_right = df[(df['pre_post']=='Post') &
                         (df['hemis']=='Right')][feature].values

    sns.set_context('poster')

    plt.figure(figsize=(5,8))
    x1, x2 = 0.5, 1.5

    for pat in pats:
        sess = df[df['patient']==pat]['sessions'].unique()
        for ses in sess:
            point_pre_left = df[(df['patient']==pat) &
                                 (df['sessions']==ses) &
                                 (df['pre_post']=='Pre') &
                                 (df['hemis']=='Left')][feature].values
            point_pre_right = df[(df['patient']==pat) &
                                 (df['sessions']==ses) &
                                 (df['pre_post']=='Pre') &
                                 (df['hemis']=='Right')][feature].values
            point_post_left = df[(df['patient']==pat) &
                                 (df['sessions']==ses) &
                                 (df['pre_post']=='Post') &
                                 (df['hemis']=='Left')][feature].values
            point_post_right = df[(df['patient']==pat) &
                                 (df['sessions']==ses) &
                                 (df['pre_post']=='Post') &
                                 (df['hemis']=='Right')][feature].values
            xdat1= x1+np.random.normal(0, 0.025, 1)
            xdat2= x2+np.random.normal(0, 0.025, 1)

            # skip if pre&post not both present (is this a good idea?)
            if point_pre_left.shape[0]==0 or point_pre_right.shape[0]==0 or point_post_left.shape[0]==0 or point_post_right.shape[0]==0:
                pass
            else:
                plt.plot([xdat1,xdat2], [point_pre_left, point_post_left], color='r', alpha=0.05, lw=5)
                plt.plot([xdat1,xdat2], [point_pre_right, point_post_right], color='b', alpha=0.05, lw=5)
                plt.scatter(xdat1, point_pre_left, color='r', alpha=0.7)
                plt.scatter(xdat2, point_post_left, color='r', alpha=0.7)
                plt.scatter(xdat1, point_pre_right, color='b', alpha=0.7)
                plt.scatter(xdat2, point_post_right, color='b', alpha=0.7)

    plt.plot([x1-0.2, x1+0.2], [np.nanmean(means_pre_left), np.nanmean(means_pre_left)], lw=7, c='r', label='left')
    plt.plot([x2-0.2, x2+0.2], [np.nanmean(means_post_left), np.nanmean(means_post_left)], lw=7, c='r')
    plt.plot([x1-0.2, x1+0.2], [np.nanmean(means_pre_right), np.nanmean(means_pre_right)], lw=7, c='b', label='right')
    plt.plot([x2-0.2, x2+0.2], [np.nanmean(means_post_right), np.nanmean(means_post_right)], lw=7, c='b')
            
    plt.xlim([0, 2])

    plt.xticks([x1, x2], ["Pre", "Post"])

    if feature == 'alphas':
        ylabel = 'Alpha Frequency (Hz)'
    elif feature == 'thetas':
        ylabel = 'Theta Frequency (Hz)'
    elif feature == 'chans_exps':
        ylabel = 'Aperiodic Exponent'
    else:
        ylabel = feature[:5]+' power'

    plt.ylabel(ylabel)
    plt.legend()

    plt.tight_layout()


def plot_hemi_feature_prepost_sessions(df, feature=''):
    """plot feature by pre/post across all 4 sessions with hemisphere

    Parameters
    ----------
    df: pandas DataFrame
        dataframe containing extracted features, averaged across hemispheres
    feature: str
        feature of interest; 'alphas', 'thetas', 'chans_exps'

    Returns
    -------
    plot: matplotlib obj
        plot of feature pre/post treatment of all sessions
    """

    pats = np.unique(df['patient'])

    plt.figure(figsize=(15,4))
    x_vals = [1, 2, 3, 4]

    for pat in pats:
        sess = df[df['patient']==pat]['sessions'].unique()
        for ses in sess:
            # get x val for plot
            if ses == 1:
                x1, x2 = x_vals[0]-0.25, x_vals[0]+0.25
            if ses == 4:
                x1, x2 = x_vals[1]-0.25, x_vals[1]+0.25
            if ses == 8:
                x1, x2 = x_vals[2]-0.25, x_vals[2]+0.25
            if ses == 12:
                x1, x2 = x_vals[3]-0.25, x_vals[3]+0.25

    
            point_pre_left = df[(df['patient']==pat) &
                                 (df['sessions']==ses) &
                                 (df['pre_post']=='Pre') &
                                 (df['hemis']=='Left')][feature].values
            point_pre_right = df[(df['patient']==pat) &
                                 (df['sessions']==ses) &
                                 (df['pre_post']=='Pre') &
                                 (df['hemis']=='Right')][feature].values
            point_post_left = df[(df['patient']==pat) &
                                 (df['sessions']==ses) &
                                 (df['pre_post']=='Post') &
                                 (df['hemis']=='Left')][feature].values
            point_post_right = df[(df['patient']==pat) &
                                 (df['sessions']==ses) &
                                 (df['pre_post']=='Post') &
                                 (df['hemis']=='Right')][feature].values
            xdat1= x1+np.random.normal(0, 0.025, 1)
            xdat2= x2+np.random.normal(0, 0.025, 1)

            # skip if pre&post not both present (is this a good idea?)
            if point_pre_left.shape[0]==0 or point_pre_right.shape[0]==0 or point_post_left.shape[0]==0 or point_post_right.shape[0]==0:
                pass
            else:
                plt.plot([xdat1,xdat2], [point_pre_left, point_post_left], color='r', alpha=0.05, lw=5)
                plt.plot([xdat1,xdat2], [point_pre_right, point_post_right], color='b', alpha=0.05, lw=5)
                plt.scatter(xdat1, point_pre_left, color='r', alpha=0.7)
                plt.scatter(xdat2, point_post_left, color='r', alpha=0.7)
                plt.scatter(xdat1, point_pre_right, color='b', alpha=0.7)
                plt.scatter(xdat2, point_post_right, color='b', alpha=0.7)


    plt.xlim([0.5, 4.5])

    plt.xticks(x_vals, ["1", "4", "8", "12"])

    if feature == 'alphas':
        ylabel = 'Alpha CF'
    if feature == 'alpha_pows':
        ylabel = 'Alpha Power'
    if feature == 'thetas':
        ylabel = 'Theta CF'
    if feature == 'theta_pows':
        ylabel = 'Theta Power'
    if feature == 'chans_exps':
        ylabel = 'Aperiodic Exponent'

    plt.ylabel(ylabel)
    plt.xlabel('Session')
    plt.legend()

    plt.tight_layout()