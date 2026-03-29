---
slug: 'programovani-s-podporou-ai'

author: Patrick Zandl
categories:
- Patrickův newsletter
- AI
- Internet
- Automotive
date: '2024-07-18'
original_newsletter: '#79: Pět úrovní umělé inteligence podle OpenAI'
summary_points:
- AI nástroje jako Claude a Copilot usnadňují programování, automatizují rutinní úkoly
  a šetří čas.
- Claude doporučila BannerGPT a Cloudinary pro generování a úpravu obrázků na webu
  Marigold.
- No-code platformy jako GitWit umožňují vytvářet aplikace z textového zadání, zjednodušují
  vývoj.
- AI má velký potenciál v testování kódu a kontrole kvality, mění budoucnost programování.
title: Programování s podporou AI
---

Musím říct, [[programování s AI](/item/programovani-s-ai/)](/item/programovani-s-ai/) za zády, to je jako mít za sebou zkušeného slušně seniorního a trpělivého programátora a devopsáka v jednom. Tak například pro [Marigold.cz](http://marigold.cz/) potřebuji občas sáhnout do šablon a upravit v nich něco, co mě štve. Například na konci titulní stránky se mi vypisovaly všechny archivní stránky, bylo jich přes 170. Jelikož Jekyll (nástroj, kterým se Marigold generuje) moc neznám, poležel bych si v dokumentaci, než bych to vyřešil, takže jsem poprosil Claude, ať to zařídí. Obratem mi dodala kus kódu, který to uspokojivě vyřešil tak, že to vypisuje jen odkaz na archivní stránku, na níž jste, tři před, tři za a skok na konec a začátek. Elegantní. 

Jsou silnější nástroje, například Copilot v Githubu nebo VS Code. Ten vám našeptává celý kód. Platí se zvláště a já to nepoužívám, ale co sleduju programátory kolem sebe, jsou z toho nadšení, protože jim to bere rutinní práci. Já používám Claude (ale stejně funguje i ChatGPT) třeba i pro řešení maličkostí, kde potřebuju i najít a doporučit službu. Například jsem chtěl přidat na titulní stránku Marigolda přidat poutací obrázky ke článkům. Jenže by dalo dost práce je vyhledat, oříznout a přidat do článků. Tak jsem opět poprosil Claude. Claude doporučila službu [BannerGPT](https://bannergpt.dabble.so/), která umožní vygenerovat ilustrační obrázky ke článkům. Pak mi navrhla mechanismus, jak obrázky pomocí GIthubu dostat na Marigolda a přes další službu [Cloudinary](https://cloudinary.com/invites/lpov9zyyucivvxsnalc5/awvly2wltpg9hdw9uq2w?t=default) obrázky změnit na správnou velikost a přitom je oříznout tak, aby zůstalo z nich vidět to podstatné. To Cloudinary umí parádně, přes AI si vybere z obrázku to důležité, takže i když mu musí změnit dramaticky stranové poměry, dává obrázek smysl. Cloudinary jsem neznal, přitom je to fajn služba na strojové zpracování obrázků, mají API, mají web rozhraní, umožňují manipulace s obrázky ze zdrojového kódu, mají i možnost postavit si obsáhlé workflow na obrázky se zpracováním všeho druhu a mají free režim zcela postačující pro můj blog včetně služeb CDN. 

No a na závěr mi Claude navrhla, jak vystavět workflow. Upřímně řečeno mi původně navrhla script v Pythonu, který by to zcela automatizoval, ale ten mi nevyhovoval, protože mi přišlo, že to nemám pod kontrolou, takže nakonec si nejlepší ilustrační obrázek vybírám a zadávám sám ručně - a zbytek už nechám dělat mechanismus navržený Claude. 

Chybí mi v tom něco? Asi to, aby Claude mohla přistupovat přes můj účet na Github a další služby, abych ji mohl k tomu autorizovat. Protože Claude mi vygeneruje zdrojový kód a řekne mi, do jaké adresářové struktury ho mám nahrát na GIT, což je jen krůček od toho, abych ji autorizoval propojení a nechal ji na GIT to všechno nahrát místo mě. Takhle je to trošičku opruz s copy&paste. 

Jsou služby, které jdou dále. Takový [GitWit](https://gitwit.dev/) vám umožní udělat appku v Reactu jen z textového zadání ještě pohodlněji, než Claude. Vyzkoušel jsem to a na jednoduché aplikace je to opravdu funkční a zajímavé. Takovéto No-Code prostředí jsou na rychlém vzestupu, ale je třeba se mírně přizpůsobit. Začít od malého kousku a postupně nabalovat, nechtít hned všechno najednou. Je tu už celá řada takových nástrojů, jako GitWit, nemusíte za ně platit, s mírným nepohodlím copy&paste si můžete programy vytvářet i v ChatGPT/Claude a dokonce si můžete nechat poradit, která služba vám je bude hostovat a jak to rozchodit. Pro malé aplikace tady cítím velký potenciál. 

Obrovský potenciál je na trhu podpory testování a kontroly kvality kódu. Je už dnes celá řada aplikací, která se vám snaží nabídnout testovací rutiny pro váš kód nebo jeho kontrolu. 

Mimochodem, zmíněný BannerGPT je postaven nad prostředním [MLBlocks](https://www.mlblocks.com/), které umožňuje vytvářet workflow nad obrázky. Například vzít vaše obrázky, vymazat z nich pozadí a dodat na ně pozadí s vaší firmou, pak to všechno někam nahrát. Všechno vizuálně, přístupem no-code.

Bude to ještě zajímává jízda v programování a mohu vám zaručit, že programování za deset let bude úplně jiné, než dneska. 

_PS: Vím, že Claude je myšleno jako mužské jméno Claude Shannona, ale já si pod tím raději představím tu chytrou francouzskou matematičku, takže budu používat ženský tvar🙂_

* * *