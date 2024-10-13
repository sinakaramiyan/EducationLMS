const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    mode: 'production',
    devtool: false,
    watch: false,

    entry: './static/js/index.js', // Your entry point for JS/CSS
    output: {
        filename: 'bundle.js', // Output JS file
        path: path.resolve(__dirname, 'static/dist/'), // Output directory
        clean: true,  // Cleans old files
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    'style-loader',
                    'css-loader',
                    'postcss-loader' // Use PostCSS for Tailwind
                ],
            },
            {
                test: /\.(png|svg|jpg|jpeg|gif|webp)$/i,
                type: 'asset/resource',
            },
            {
                test: /\.(woff|woff2|eot|ttf)$/i,
                type: 'asset/resource',
                generator: {
                    filename: 'fonts/[name][ext][query][contenthash:8]', // Add contenthash
                },
            },
        ],
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: 'style.css', // Output CSS file
        }),
        new BundleTracker({ 
            path: path.resolve(__dirname, './static/dist/'),
            filename: 'webpack-stats.json' 
        })
    ],
};