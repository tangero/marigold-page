---
author: Patrick Zandl
categories:
- Mobilní sítě
- LTE
- 5G
hide: true
layout: post
post_excerpt: Integrated Access and Backhaul (IAB) - Integrované přístupové a páteřní
  propojení.  Jde o technologii, která má potenciál dramaticky změnit způsob, jakým
  jsou navrženy a nasazeny mobilní sítě.
summary_points:
- IAB integruje přístup a páteřní propojení v 5G sítích.
- IAB architektura zahrnuje IAB donor, nodes, MT (Mobile Termination) a DU (Distributed
  Unit).
- IAB nabízí rychlejší nasazení 5G, flexibilitu, lepší pokrytí a efektivní využití
  spektra.
- Budoucí IAB zlepší směrování pomocí AI/ML a podpoří Non-Terrestrial Networks (NTN).
title: Integrated Access and Backhaul (IAB) v sítích 5G
---

Jednou z nejzajímavějších inovací v 3GPP Release 16, finalizované v roce 2020 je [[Integrated Access and Backhaul](/item/integrated_access_and_backhaul_iab_5G/)](/item/integrated_access_and_backhaul_iab_5G/) ([[IAB](/item/integrated_access_and_backhaul_iab_5G/)](/item/integrated_access_and_backhaul_iab_5G/)) - Integrované přístupové a páteřní propojení.  Jde o technologii, která má potenciál dramaticky změnit způsob, jakým jsou navrženy a nasazeny mobilní sítě. IAB představuje elegantní řešení pro jeden z největších problémů při nasazování 5G sítí: potřebu husté infrastruktury a nákladného backhaulu, tedy páteřního propojení. To se v 3G sítích realizovalo zpravidla mikrovlnými pojítky nebo metalickými propojeními, u 4G sítí stoupaly nároky na jeho kvalitu až k gigabitovým optickým linkám.  

## Co je IAB

IAB je technologie, která umožňuje základnovým stanicím (gNB) využívat stejné rádiové rozhraní jak pro komunikaci s uživatelskými zařízeními (UE), tak pro páteřní připojení k páteřní síti. Jinými slovy, IAB node může fungovat současně jako přístupový bod pro mobilní zařízení a jako relay pro přenos dat do a z páteřní sítě. To samozřejmě neznamená, že by bylo nutné používat stejné frekvenční pásmo, IAB umožňuje použít jiné frekvenční pásmo pro připojení uživatelského zařízení a jiné pro propojení na jiný přístupový bod. Typické je, že pro propojení mezi IAB nody/donory se používá pásmo mmWave, typicky 28 GHz v městských oblastech, v méně hustě osídlených oblastech pak sub-6 GHz. V některých případech může IAB využívat kombinaci licencovaných pásem pro kritické spojení a nelicencovaných pásem (např. 5 GHz Wi-Fi pásmo) pro doplňkovou kapacitu. IAB může využívat techniku Carrier Aggregation k kombinaci různých frekvenčních pásem pro zvýšení celkové kapacity backhaulu. 

## Architektura IAB

IAB architektura se skládá z několika klíčových komponent:
1. IAB donor: Toto je gNB s přímým připojením k páteřní síti (obvykle přes optické vlákno).
2. IAB nodes: Tyto uzly fungují jako relays, přijímající backhaul připojení od IAB donoru nebo jiných IAB nodes a poskytující přístup UE.
3. IAB-MT (Mobile Termination): Část IAB node, která komunikuje s nadřazeným uzlem (donor nebo jiný IAB node).
4. IAB-DU (Distributed Unit): Část IAB node, která poskytuje rádiové rozhraní pro UE nebo podřízené IAB nodes.

![IAB architektura](/assets/iab-architektura.jpg)

## Srovnání s předchozími technologiemi

V čem představuje IAB významný pokrok oproti předchozím přístupům k řešení backhaulu v mobilních sítích?  Klasické backhaul řešení v 3G a 4G sítích jako mikrovlnné spoje nebo optická vlákna vyžadují dodatečnou infrastrukturu a značné investice. LTE již dříve v Release 10 zavedlo koncept **Relay Nodes**, ale ty byly omezené ve své funkčnosti a flexibilitě. IAB rozšiřuje tento koncept, umožňuje multi-hop topologie a poskytuje mnohem větší flexibilitu v síťovém plánování. Navíc využívá existující 5G rádiové rozhraní, což významně snižuje náklady a zjednodušuje nasazení. 

Podobně je to s konceptem **Small Cells**. Ty zlepšily pokrytí a kapacitu v hustých oblastech, stále ale vyžadovaly samostatné backhaul řešení. Zatímco základy pro Small Cells byly položeny již v Release 8 s konceptem HeNB (tedy Home eNodeB), plnohodnotný koncept Small Cells, jak jej známe dnes, se vyvíjel především od Release 10 ([[LTE-Advanced](/mobilnisite/3gpp-release-10/)](/mobilnisite/3gpp-release-10/)) a dále. Každý následující release přidával nové funkce a vylepšení, která zvyšovala efektivitu a flexibilitu nasazení Small Cells.

Je dobré poznamenat, že termín "Small Cells" se stal běžně používaným v průmyslu kolem roku 2011-2012, což koresponduje s obdobím Release 10 a 11. Small Cell Forum, klíčová průmyslová organizace propagující tuto technologii, byl založen v roce 2007 (původně jako Femto Forum) a přejmenován na Small Cell Forum v roce 2012, což odráží širší adopci tohoto konceptu v mobilních sítích. Odtud tedy můžeme tušit i zájem o další rozvoj do směru IAB, kdy IAB integruje backhaul přímo do small cell konceptu. 

## Klíčové výhody IAB

Pojďme si shrnout klíčové výhody IAB v 5G sítích. 
1. Rychlejší a levnější nasazení 5G - IAB umožňuje operátorům rychle rozšířit pokrytí 5G bez nutnosti budovat nákladnou backhaul infrastrukturu.
2. Flexibilita v síťovém plánování - Operátoři mohou dynamicky přidávat nebo přesouvat IAB nodes podle potřeby, což umožňuje rychlou reakci na měnící se požadavky na pokrytí a kapacitu.
3. Zlepšené pokrytí - IAB umožňuje rozšíření 5G pokrytí do oblastí, kde by bylo obtížné nebo nákladné instalovat tradiční backhaul.
4. Efektivní využití spektra - Díky dynamickému přidělování zdrojů mezi přístupem a backhaulem může IAB optimalizovat využití dostupného spektra. Jedním z výzkumů pro budoucí sítě je právě efektivita využití spektra a její zvyšování pomocí ML/AI. 
5. Podpora pro mmWave - IAB je zvláště užitečné pro mmWave nasazení, kde je omezený dosah kompenzován možností multi-hop přenosů.

## Technické aspekty IAB

1. Topologie - IAB podporuje jak stromové, tak mesh topologie, což umožňuje vysokou flexibilitu v síťovém designu.
2. Směrování - IAB implementuje sofistikované směrovací algoritmy pro optimalizaci cest v multi-hop scénářích.
3. Adaptivní alokace zdrojů - Systém dynamicky rozděluje rádiové zdroje mezi přístup (UE) a backhaul (MT) funkce podle aktuálních potřeb.
4. Synchronizace - IAB zavádí pokročilé synchronizační mechanismy pro zajištění přesné časové a frekvenční synchronizace napříč multi-hop topologií.
5. QoS management - IAB podporuje end-to-end QoS, zajišťující, že kritické služby mají prioritu i v multi-hop scénářích.

Ale také je dobré říct si na rovinu, že IAB má své stinné stránky a nevýhody, byť možná potenciální. Tak především latence, na kterou sítě 5G tlačí. S rostoucím počtem hopů může narůstat, což může být pro některé use cases problematické. Stejně tak sdílení zdrojů mezi radiovou přístupovou sítí a backhaulem může vést k omezení celkové kapacity sítě použitelné pro rychlé přenosy. Další rizika představují interference na rádiové vrstvě, snížená energetická účinnost a také bezpečnost. Multi-hop topologie představují bezpečnostní výzvy a vyžadující robustní šifrovací i autentizační mechanismy.

## Budoucí vývoj

Zatímco IAB představuje významný pokrok v Release 16, budoucí vydání 3GPP přinesou další vylepšení:

1. Inteligentní IAB (Release 17 a dále) - Očekává se integrace AI/ML algoritmů pro optimalizaci směrování, alokace zdrojů a QoS managementu v IAB sítích.
2. Rozšířená podpora pro [[Non-Terrestrial Networks](/mobilnisite/non-terrestrial-networks-ntn-5G-nezemske-site/) ([NTN](/mobilnisite/non-terrestrial-networks-ntn-5G-nezemske-site/))](/mobilnisite/non-terrestrial-networks-ntn-5G-nezemske-site/) Budoucí Release zřejmě rozšíří IAB koncept na satelitní a vzdušné platformy (tedy [Non-Terrestrial Networks](/mobilnisite/non-terrestrial-networks-ntn-5G-nezemske-site/) ([NTN](/mobilnisite/non-terrestrial-networks-ntn-5G-nezemske-site/))), umožňující ještě větší flexibilitu v poskytování konektivity. Zatím s tím počítejme tak do Release 19, spíše 20. 
3. Vylepšené multi-RAT integrace - Budoucí verze IAB mohou lépe integrovat různé rádiové přístupové technologie, včetně Wi-Fi a budoucích 6G systémů.

## Praktické nasazení IAB

Verizon byl jedním z prvních operátorů, který oznámil plány na využití IAB pro rozšíření svého mmWave 5G pokrytí. Společnost využívá IAB především v městských oblastech pro zlepšení pokrytí a kapacity bez nutnosti rozsáhlých investic do fiber backhaulu. China Mobile využívá IAB pro rozšíření 5G pokrytí v hustě osídlených městských oblastech i v odlehlejších venkovských lokalitách. Asi největším zastáncem IAB je ale japonský Rakuten Mobile. Jako nový operátor s plně virtualizovanou sítí, Rakuten Mobile intenzivně využívá IAB pro rychlé budování své 5G infrastruktury. Ve Francii Orange testuje IAB jako způsob, jak překlenout "digitální propast" a poskytnout vysokorychlostní 5G připojení v oblastech, kde je obtížné nebo nákladné instalovat tradiční backhaul.

Integrated Access and Backhaul (IAB) představuje významný krok vpřed v evoluci 5G sítí. Tato technologie elegantně řeší jeden z největších problémů při nasazování 5G – potřebu husté infrastruktury a nákladného backhaulu. Díky své flexibilitě, škálovatelnosti a nákladové efektivitě má IAB potenciál urychlit adopci 5G, zejména v mmWave pásmech a díky tomu v oblastech, kde je obtížné nebo nákladné instalovat tradiční backhaul řešení.

Zatímco IAB není bez výzev, jeho výhody jasně převažují nad omezeními. S pokračujícím vývojem a optimalizací v budoucích vydáních 3GPP se očekává, že IAB se stane klíčovou technologií nejen pro 5G, ale i pro budoucí generace mobilních sítí.

Už teď je zřejmé, že IAB není jen přechodným řešením, ale fundamentální změnou v přístupu k návrhu a nasazení mobilních sítí. S rostoucí poptávkou po všudypřítomné vysokorychlostní konektivitě a s výhledem na budoucí technologie jako 6G, bude role IAB v telekomunikačním ekosystému pravděpodobně ještě významnější.

V konečném důsledku IAB představuje více než jen technologickou inovaci – je to nástroj, který má potenciál demokratizovat přístup k vysokorychlostnímu internetu, překlenout digitální propast a umožnit nové use cases a služby, které budou formovat naši digitální zkušenost.