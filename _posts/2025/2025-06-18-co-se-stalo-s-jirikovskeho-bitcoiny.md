---
author: Patrick Zandl
categories:
- bitcoin
- krypto
- kryptoměny
- Jiříkovský
- Pavel Blažek
layout: post
post_excerpt: Konečně se vyjasnilo, co se stalo s chybějícími devíti miliardami korun v bitcoinech z darknetového tržiště Nucleus Market. Soudní znalec Jiří Berger, který byl přítomen otevírání bitcoinové peněženky, vysvětlil, co se stalo s my se spolu detailně podíváme na to, kdo má radost a kdo méně. 
thumbnail: https://www.marigold.cz/assets/babis-bitcoin.png
title: "Víme, co se stalo s 9 miliardami korun Tomáše Jiříkovského z tržiště Nucleus"
---

Konečně se vyjasnilo, co se stalo s chybějícími devíti miliardami korun v bitcoinech z darknetového tržiště Nucleus Market. Soudní znalec Jiří Berger, který byl přítomen otevírání bitcoinové peněženky, vysvětlil, co se stalo s my se spolu detailně podíváme na to, kdo má radost a kdo méně. 

Nejprve začneme více laickým vysvětlením, technicky exaktnější vysvětlení si dáme na závěr pro zájemce. 

Zádrhel je v tom, že Jiříkovského peněženka používala ještě **starší verzi Bitcoin Core, založenou na technologii JBOK**, ne na modernější technologii HD. Hlavním problémem této technologie bylo zálohování. Zálohou JBOK je totiž možné zpřístupnit jen ty adresy z peněženky, které vznikly do doby vzniku zálohy. Nelze tak zpřístupnit prostředky, které jsou na adresách vzniklých až po vzniku zálohy. V praxi to znamená, že **soudní znalec konstatoval, že použitím zálohy je zpřístupněno oněch 1561 BTC**, z nichž stát dostal slíbených 30 %. Soudní znalec **na policií vrácených počítačích jiné klíče nenalezl** a tudíž jiné adresy nebylo možno obnovit.  A pokud se nenajde novější záloha na jiném hardware, tak u toho výsledku také zůstane. 

Jakékoliv jiné prostředky jsou bez zálohy klíče nedostupné, ačkoliv jsou v blockchainu vidět. Médii zmiňovaných 3855,15 BTC je tedy pravděpodobně _"ztraceno"_ - nelze s nimi nijak nakládat. 

### Jak si to představit? 

Představte si bitcoinovou peněženku jako skříň, která má více přihrádek - a každou z nich zamyká unikátní klíč. Při záloze se vytvoří kopie klíčů. Jenže se dělá jen kopie klíčů, které existují k tomuto datu. Pokud se po tomto datu do skříně přidají další zamykatelné přihrádky, kopie klíčů od nich v původní záloze neexistují a je nutné je znovu vytvořit. A to je to, co se stalo - na vydávané technice byla kopie klíčů k určitému datu, jíž se podařilo zpřístupnit část přihrádek. Ostatní klíče prostě nejsou k dispozici. 

Teď víte všechno, co potřebujete vědět. Jiříkovský se dostal k té části peněz, od které měl klíče a ke zbytku se s technikou, kterou od státu dostal zpět, nedostane. Dokud se nenajdou další klíče, jsou tyto prostředky ztraceny, což je ostatně u "starých" bitcoinů dosti běžný stav. 

### Podrobnější technické vysvětlení

Nyní se na záležitost podíváme pro zájemce více exaktně pro technicky orientované zájemce. Ostatní mohou přeskočit na politický závěr. 

Za prvé je třeba si vyjasnit **vztah mezi pojmy peněženka a adresa** v případě kryptoměn. 
- **Peněženka** je soubor privátních klíčů, v tomto případě reprezentovaná souborem wallet.dat. 
- **Adresa** proti tomu je onou přihrádkou v peněžence a v peněžence jich může být nekonečně mnoho.

Tradičně se **pro každou transakci generuje nová adresa**, čímž se přispívá k _pseudonymitě_ bitcoinu. Adresy totiž nejsou bez klíče nijak propojitelné mezi sebou, z jednotlivých adres není poznat, že pocházejí ze stejné peněženky. 

K tomu, abyste potvrdili s naprostou jistotou příbuznost adres, potřebujete buďto privátní klíč nebo XPUB (ten ovšem až po polovině 2016!), tedy rozšířenou verzi veřejného klíče. V případě adres atributovaných na Nucleus Market ale nemáme ani jedno. 

Nucleus Market přesně takto ke generování adres přistupoval. Pro každou trasakci, tedy například platbu za zboží, vygeneroval jedinečnou adresu, díky čemuž také prodávající snadno mohl ověřit, že peníze skutečně jsou v úschově a mohl bez obav odeslat zboží. Celkem je tak s Nucleus Market spojeno 164 860 adres, musí tedy existovat stejné množství klíčů, jinak není možné všechny tyto adresy otevřít a část prostředků se ztratí. Nelze také s jistotou říct, že všechny tyto adresy ovládá jedna osoba přes jednu peněženku, adresy (a jejich klíče) mohou být uspořádány jinak. Zejména u JBOK typu peněženek je velmi důležité datum jejího zálohování, jak už jsme si vysvětlili.

Podívejme se, **jak se dospělo k těm cca 165 tisícům adres**, které jsou dnes chápány jako adresy Nucleus Marketu. Už víme, že pokud nemáme privátní klíč, nelze ověřit, že tyto adresy patří do jedné peněženky - a privátní klíč nemáme. Proto se používá heuristická analýza s různou mírou spolehlivosti. Tak například se posbíraly prvotní adresy, které o sobě Nucleus zveřejnil na své onion stránce či při různých nákupech, které se daly dohledat - např. účastníci transakce poskytli adresu. Tyto adresy lze velmi jistě s Nucleus Market spojit. 
Druhý důležitý postup je současný podpis. Při platbě bitcoinem je běžné, že se používají prostředky ze dvou či více adres v jedné peněžence. Když máte zaplatit 3 BTC, které máte v jedné peněžence, pravděpodobně je ale máte na více adresách. Když dvě nebo více adres podepíšou stejnou odchozí platební transakci, musí jejich privátní klíče držet jedna entita. Pokud je některá z adres věrohodně připisována k Nucleusu, lze i ostatní adresy v transakci považovat za stoprocentně spojitelné s Nucleus tržištěm. 

Existují i další postupy a díky nim se vytvořila ona databáze 165 000 adres, které jsou dnes velmi přesvědčivě považovány za adresy Nucleus Market. Mimochodem, tento typ analýzy v USA běžně obstojí při podpoření dalšími důkazy v soudím procesu a považuje se za vysoce průkazný. Jen je zdlouhavý. Je ale také nutné připustit, že nejrůznějšími vlivy mohlo dojít k chybné atribuci. Především se již v té době používaly mixéry, které umožňují složit transakci z více adres různých vlastníků, což má přerušit forenzní řetězec. Mixéry a například technologie CoinJoin by značně ztížily forenzní analýze možnost přiřadit adresy k jednomu vlastníku. U Nucleus Marketu se ale do roku 2016 míchací techniky prakticky v on-chain datech neobjevují. Transakce probíhaly jako běžné platby, takže heuristiky mohly s pravděpodobností kolem 95 % spojit cca 165 000 adres bez znalosti XPUB. Kdyby provozovatelé masově nasadili tumbler nebo důsledný CoinJoin, přesnost clustrování by klesla na desítky procent a část adres by zůstala mimo shluk. I tak ale je potřeba poznamenat, že několik tisícovek adres se do shluku Nucleus Market dostalo neoprávněně. Velmi pravděpodobně to ale nejsou žádné zásadní částky a všechny klíčové adresy zcela průkazně do shluku Nucleusu patří oprávněně. 

Proto také různé zdroje udávají různá čísla: [Bitinfochart spojuje Nucleus](https://bitinfocharts.com/bitcoin/wallet/NucleusMarket) s oněmi 165000 adresami, [Arkham počítá](https://intel.arkm.com/explorer/entity/nucleus-marketplace) spíše s 146000 adresami. Rozptyl je tedy dost velký. Podstatné je, že webové stránky udávají součet prostředků ze všech atribuovaných adres, ale klíče nemusí být od všech adres dostupné. 

Pro nás je podstatné, že po uzavření tržiště proběhly převody jen s malým počtem adres, podle údajů na Arkham a WalltetExplorer šlo o cca 6500 adres. To jsou v naprosté většině ty adresy, s nimiž manipuloval Jiříkovský v roce 2025, jejich obživnutí ostatně způsobilo v kryptoměnovém světě slušnou senzaci. Mezi lety 2017 a 2024 přitom na _"žádné"_ z adres Nucleus Marketu neproběhly žádné transakce. Proč uvozovky kolem slova _"žádné"_? Ve skutečnosti proběhlo několik ojedinělých vkladových transakcí, které se označují jako "dust" a byly pokusem k ospamování darknet tagů, tedy ospamování oné atribuce peněženek s Nucleus Market. 

Tak a to už je skoro všechno, co bylo potřeba si k celé záležitosti říct. Na počítačích vydaných policií byly klíček adresám obsahujícím 1561 BTC, o které se Jiříkovský se státem rozdělil dle dohody. K ostatním adresám nebyly klíče nalezeny a nebylo možné z nich tedy provádět žádné převody. A jelikož ani dnes, když je Jiříkovský za kopečky, nejsou na těchto adresách žádné převody, je možné tyto peněženky považovat nadále jako "dormant", tedy spící a pravděpodobně také za ztracené. Ačkoliv nelze vyloučit variantu, že je někdo ovládá a moudře vyčkává, až se usadí rozruch - jenže v tom případě klíče k těmto peněženkám nepocházejí z techniky zabavené státem a někdo vydržel už hodně dlouho čekat.

**A na závěr poznámka pro šťouraly.** Tento popis platí pro technologii Bitcoin Core 0.12 a nižší, tedy na technologii, kterou v roce 2014 používal Jiříkovský. V srpnu 2016 vyšel Core 0.13, který zavedl HD klíče, tedy hierarchicky determinované klíče. U nich již není možné ztratit klíče k jednotlivým peněženkám, protože jsou odvozovány a vždy zpětně odvoditelné od master klíče, master seedu. Lze ztratit jen celou peněženku (tedy master seed). 

### Politický závěr - co z toho plyne?

Teď jsme si ujasnili technické pozadí. Zatímco na webovém rozhraní to vypadá, že se s peněženkou Nucelusu pracuje, živé jsou jen některé adresy. Soudní znalec zjistil klíče k adresám obsahujícím cca 1561 BTC a ty byly rozděleny. Až potud je tedy vše v pořádku a histerie, kterou rozpoutává paní Schillerová, není na místě. 

Na místě je otázka, proč není vyšetřován Jiříkovský za trestné činy ve spojitosti s Nucleus Market, když je zcela průkazné, že jeho peněženku ovládá a o činnosti tohoto tržiště není pochyb. Ministerstvo k tomu mělo dát podnět, důvodů k tomu mělo hodně - a orgány činné v trestním řízení měly "konat", ne nechat podezřelého vycestovat tam, odkud už se asi nevrátí. Tady to vypadá, že ministerstvo spravedlnosti některé informace, které mu byly známy, policii a soudům prostě nesdělilo, aby byl hardware v rozporu s původními usneseními vrácen. 

Obhajoba bývalého ministra Blažka, že stát není "povinným v rámci AML", tedy není povinen prověřovat původ peněz, je sice pravdivá, ale neobstojí. Stát nemá co přijímat dar pocházející z trestné činnosti, stát má takové peníze zabavovat. V tom je dost podstatný rozdíl. A už vůbec není možné, aby stát přistupoval k tak ožehavým záležitostem tak diletantsky, protože to likviduje víru lidí v kompetenci politické reprezentace. 