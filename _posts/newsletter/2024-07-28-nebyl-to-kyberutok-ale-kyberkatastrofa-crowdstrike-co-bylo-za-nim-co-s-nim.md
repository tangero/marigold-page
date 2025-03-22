---
author: Patrick Zandl
categories:
- Patrickův newsletter
- Apple
- Microsoft
- AI
- Internet
- Bezpečnost
- Česko
- EU
- Automotive
date: '2024-07-28'
layout: post
original_newsletter: '#80: Kyberkatastrofa Crowdstrike'
summary_points:
- Globální výpadek způsobila chybná aktualizace softwaru Falcon od Crowdstrike.
- Problém postihl platící zákazníky Crowdstrike, paradoxně ty zodpovědnější.
- Microsoft se dříve pokusil omezit přístup k jádru, ale narazil na odpor.
- Šéf Crowdstrike, George Kurtz, zažil podobnou havárii i ve firmě McAfee.
title: ☠️ Nebyl to kyberútok, ale kyberkatastrofa. Crowdstrike. Co bylo za ním, co s ním?
---

Chvíli to páteční ráno vypadalo jako vydařený kyberútok. Zapnuté počítače náhle nebyly schopné zavést operační systém a hroutily se do modré obrazovky smrti. Pracovníci bank, nemocnic a dalších institucí se nemohli dostat do počítačů. V Austrálii havarovaly samoobslužné pokladeny. Ve Velké Británii musela televize Sky News přerušit vysílání poté, co začaly havarovat servery a počítače na odbavovacích pracovištích. V Hongkongu a Indii začaly selhávat odbavovací přepážky na letištích. Než nastalo ráno v USA, zhroutily se miliony počítačů se systémem Windows a nastala globální technická katastrofa.

[![](https://substack-post-media.s3.amazonaws.com/public/images/a58cf4ac-f47c-4d96-8029-154a2c9cd5fb_708x398.heic)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa58cf4ac-f47c-4d96-8029-154a2c9cd5fb_708x398.heic)

![](https://substack-post-media.s3.amazonaws.com/public/images/a58cf4ac-f47c-4d96-8029-154a2c9cd5fb_708x398.heic)

Záhy se ukázalo, že ačkoliv je podezřelé, že nedotčené jsou počítače v Číně, Rusku nebo Íránu, o žadnou úmyslou sabotáž z těchto zemí nejde. Za chybu mohl software Falcon dodávaný firmou Crowdstrike, který má chránit počítače před průniky a hackery. Služba je placená a pro země jako Írán nebo Rusko není kvůli sankcím dostupná. To byl také důvod, proč se katastrofa nedotkla každého. Paradoxně postihla jen bohatší zákazníky, kteří dbají na svou bezpečnost a kteří si za lepší ochranu své sítě platí právě Crowdstrike a používají její software Falcon. A ty, kteří měli svůj počítač online zhruba mezi šestou a půl osmou středoevropského času.

Technicky je to velmi zajímavý problém. Microsoft poskytuje možnost vybraným programům pracovat na úrovni jádra operačního systému, tedy obejít ochranné mechanismy ve Windows. Tak pracuje i ovladač Crowdstrike Falcon. Je to důležité proto, aby Falcon mohl detekovat podezřelé chování na nejnižší úrovni v systému a odhalit potenciální hrozby. Jenže onoho pátečního rána firma vydala aktualizaci, která probudila dosud neodhalenou chybu v kódu Falconu, když požádala o přístup do neexistující adresy v paměti. Tím zhavaroval program běžící na úrovni jádra a tím i celý systém. A protože šlo o ovladač kritické důležitosti, který Windows při zavádění nomohou obejít, vždy se při zavádění systému dostanou Windows do téže situace. . Zjednodušeně řečeno program pracující na úrovni jádra nesmí nikdy spadnout. A teď spadl.

Crowdstrike si zádrhele povšiml relativně rychle a 78 minut po vydání závadné aktualizace již vydává opravu, jenže počítače, které se již aktualizovaly, je nutné ručně a nepříliš intuitivně opravit. Za oněch 78 minut stihlo zhavarovat přes 8,5 milionů počítačů včetně serverů cloudové služby Azure - a to stačilo na katastrofu.

Na celé události je poučných několik momentů a vyplatí se u nich zastavit.

Především zmíněný paradox, že **výpadek postihl společnosti, které poměrně zodpovědně připlácely za ochranu svých počítačů**. Polovina z firem v žebříčku Fortune 1000 byla mezi poškozenými, zatímco v Česku se to dotklo spíše korporací se zahraničními majiteli. Je paradoxní, když se závada nedotkne těch, kdo jsou ke kyberbezpečnosti laxní a naopak postihne zodpovědnější. Mimochodem, podobný software, jakým je Falcon, dodává i [Microsoft pod názvem Defender](https://www.microsoft.com/cs-cz/windows/comprehensive-security), je velmi dobrý jako součást Microsoft 365.

Od tohoto poznatku je blízko k úvaze, **jak se něco takového mohlo stát**. S ohledem na to, že nejsou známy mechanismy, jaké používá Crowdstrike pro kontrolu svých aktualizací, je spíše jen prostor pro spekulace a údiv nad tím, že firma, která dodává řešení pro kyberbezpečnost, sama nemá kvalitně podchycený bezpečný mechanismus testování a distribuce aktualizací. Bývá zvykem takové aktualizace důkladně testovat interně a také je uvolňovat postupně, aby havarovaných počítačů nebylo příliš. Ospravedlnilo masové vydání aktualizace toto riziko, bylo by důležitější ihned celosvětově zavést novou detekci hrozeb, nebo ji bylo lépe uvolňovat postupně a předejít velké havárii? Smůlou Crowdstrike bylo, že se mu sešla starší chyba zanesená do systémů v dubnu s novou bezpečnostní aktualizací šablon pro rychlou reakci. Firma problematiku analyzuje a navrhuje řešení v dokumentu Předběžný přezkum po incidentu, jenže už má z ostudy kabát.

Otázka je, jestli **mohl dělat něco Microsoft** , respektive samotná Windows. Uživatelů MacOS nebo Linuxu se totiž problém nedotknul, ačkoliv i pro ně Falcon existuje. Důvod je triviální, v těchto systémech je uzamčený přístup k jádru systému a Falcon je zde obyčejný proces, který když spadne, tak ho systém „odstřelí“ bez havárie sebe sama. Nabízí se otázka, zda něco podobného nemůže být i ve Windows. Inu, může. Ironií osudu ale je, že přesně o to se Microsoft pokusil již dříve u systému Windows Vista, ale narazil na odpor dodavatelů kybernetické bezpečnosti a regulačních orgánů EU.

Společnost Microsoft se v roce 2006 pokusila implementovat do systému Windows Vista funkci omezující přístup třetích stran k jádru. Dvě velké antivirové společnosti McAfee a Symantec se tehdy vzbouřily a stěžovaly si u Evropské komise. Microsoft nakonec ustoupil a opět umožnila dodavatelům bezpečnostních řešení přístup k jádru pro účely sledování bezpečnosti. Apple si takové servítky nebral a v roce 2020 zablokoval přístup vývojářů k jádru macOS.

A ta čtvrtá úvaha? **Šéf Crowdstrike George Kurtz je smolař** , protože podobná havárie se za jeho panování podařila již v minulosti. V roce 2010, kdy byl Kurtz technickým ředitelem společnosti McAfee, vydala firma aktualizaci svého antivirového software, která odstranila klíčový soubor systému Windows a způsobila rozsáhlé výpadky systému svých klientů. A stejně, jako v tomto případě, byla nutná ruční oprava. O několik měsíců později společnost McAfee koupil Intel, Kurtz záhy odchází a zakládá Crowdstrike, dnes firmu s třímiliardovým dolarovým obratem. Firemní kulturu, kvůli které tehdy údajně z McAfee odcházel, ale zjevně jeho nová firma podědila. Jestli bylo něco zásadně špatně, tak systém vydávání aktualizací - jak v McAfee, tak v Crowdstrike.

Pátá úvaha na své rozuzlení nechá teprve čekat. Bude zajímavé sledovat, **jak se Crowdstrike postaví ke své zodpovědnosti za ztrátu svých zákazníků**. Z právního pohledu je firma z obliga, protože její odpovědnost je podle podmínek služby omezena pouze na výši zaplacených poplatků. Což leteckým společnostem, které ten den zrušily 5000 letů a budou muset vyplácet tučné kompenzace, moc nepomůže.

Akcie společnosti Crowdstrike spadly z 350 dolarů na 260 dolarů a zatím zde týden setrvávají. Shodit osm milionů počítačů největších firem je v bezpečnostní branži takový malý „upsík“ a pokud se vedení podaří investory přesvědčit, že se z nehody firma poučila a přijala patřičná zlepšení, nakonec z toho bude i slušná reklama. Protože nejhorší na trhu je, když se o vás nemluví.

* * *