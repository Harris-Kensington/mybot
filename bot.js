const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
    console.log('I am ready!');
});

client.on('message', message => {
    if (message.content === 'test') {
        const embed = new Discord.RichEmbed()
        .setAuthor('Percy Bot', 'https://orig00.deviantart.net/9ce2/f/2014/201/1/7/profile_picture_by_alexthestooge-d7rk74y.png')
        .setColor(0x00AE86)
        .setDescription('This is the description of your embed message')
        .setFooter('© WilliamJPercy#8066', 'https://orig00.deviantart.net/9ce2/f/2014/201/1/7/profile_picture_by_alexthestooge-d7rk74y.png')
    }
});

// THIS  MUST  BE  THIS  WAY
client.login(process.env.BOT_TOKEN);
