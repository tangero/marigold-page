---
slug: "bgf"
url: "/mobilnisite/slovnik/bgf/"
type: "slovnik"
title: "BGF – Border Gateway Function"
date: 2025-01-01
abbr: "BGF"
fullName: "Border Gateway Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bgf/"
summary: "Border Gateway Function (BGF) je hraniční řadič relací v subsystému IP multimédií (IMS), který spravuje multimediální provoz na hranicích sítě. Poskytuje funkce vynucování politik, průchodu NAT a zabe"
---

BGF je hraniční řadič relací v subsystému IP multimédií (IMS), který spravuje multimediální provoz na hranicích sítě a poskytuje vynucování politik, průchod NAT a zabezpečení pro multimediální relace.

## Popis

Border Gateway Function (BGF) je kritická komponenta v architektuře subsystému IP multimédií (IMS) podle 3GPP, speciálně navržená pro zpracování funkcí v rovině médií na hranicích sítě. Funguje jako specializovaný hraniční řadič relací, který se nachází mezi různými administrativními doménami, například mezi IMS sítí operátora a externími IP sítěmi nebo mezi různými operátorskými sítěmi. BGF je zodpovědný za řízení a správu toku multimediálního provozu (hlas, video, text v reálném čase) na základě politik přijatých od funkce Policy and Charging Rules Function (PCRF) přes rozhraní Gq'. Implementuje schopnosti hluboké kontroly paketů k identifikaci a klasifikaci mediálních toků, což umožňuje přesné vynucování politik a správu kvality služeb.

Architektonicky se BGF skládá z několika funkčních komponent včetně zpracovatelů médií, bodů vynucování politik, bezpečnostních bran a systémů pro správu provozu. Funguje jak v přístupové, tak v jádrové části sítě – Access BGF (A-BGF) zpracovává provoz na hranici přístupové sítě, zatímco Interconnect BGF ([I-BGF](/mobilnisite/slovnik/i-bgf/)) spravuje provoz mezi různými operátorskými sítěmi. BGF zakládá a udržuje multimediální relace na základě parametrů Session Description Protocol (SDP) vyjednaných během zřizování relace a může tyto parametry podle potřeby upravovat pro průchod [NAT](/mobilnisite/slovnik/nat/) a firewallem. Udržuje informace o stavu relace pro všechny aktivní multimediální relace, které jím procházejí, včetně alokace šířky pásma, informací o kodeku a bezpečnostních asociací.

Provoz BGF zahrnuje několik klíčových procesů: zaprvé přijímá rozhodnutí o politikách od PCRF obsahující pravidla pro zpracování médií, alokaci šířky pásma a parametry účtování. Zadruhé kontroluje příchozí multimediální pakety, aby identifikoval relace a aplikoval příslušné politiky. Zatřetí provádí potřebné úpravy médií, jako je NAT, komprese hlaviček nebo transkódování, pokud je to vyžadováno. Začtvrté monitoruje kvalitu relace a může spouštět události zpět směrem k PCRF, pokud jsou překročeny prahové hodnoty kvality. BGF komunikuje s více síťovými prvky včetně Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)) pro koordinaci řízení relací, PCRF pro řízení politik a různými účtovacími funkcemi pro účely fakturace. Jeho pozice v cestě médií mu umožňuje poskytovat podrobná měření a reportování jak pro provozní, tak pro fakturační účely.

Pokud jde o bezpečnostní funkce, BGF implementuje schopnosti firewallu k ochraně jádra IMS před externími hrozbami, včetně útoků typu denial-of-service a pokusů o neoprávněný přístup. Může ověřovat mediální toky, kontrolovat, zda multimediální provoz odpovídá zřízeným relacím, a zabraňovat převzetí médií nebo krádeži služby. BGF také podporuje možnosti zákonného odposlechu vyžadované regulačními rámci a poskytuje přístup k mediálním tokům pro účely autorizovaného monitorování. Jeho schopnost skrývat topologii vnitřní sítě pomocí funkcí NAT přidává další vrstvu zabezpečení tím, že brání externím subjektům v poznání schémat interního IP adresování.

BGF hraje klíčovou roli při umožňování multimediálních služeb napříč heterogenními sítěmi tím, že řeší problémy interoperability související s různými adresními prostory sítí, bezpečnostními politikami a mechanismy kvality služeb. Zajišťuje, že kvalita médií je udržována v souladu se smlouvami o úrovni služeb, i když provoz prochází více administrativními doménami. Komplexní schopnosti BGF v oblasti zpracování médií z něj činí nezbytnou komponentu pro operátory zavádějící služby založené na IMS, zejména pro voice over LTE (VoLTE), videohovory a rich communication services (RCS).

## K čemu slouží

Border Gateway Function byla vytvořena, aby řešila několik kritických výzev v poskytování IP multimediálních služeb přes hranice sítí. Když operátoři začali zavádět architektury IMS pro multimediální služby, narazili na významné problémy s mezidoménovou konektivitou, bezpečnostními zranitelnostmi na okrajích sítě a nekonzistentní kvalitou služeb při přechodu multimediálního provozu přes administrativní hranice. Tradiční směrovače a firewally postrádaly povědomí o relacích a granularitu vynucování politik potřebnou pro služby multimédií v reálném čase, což vedlo ke špatnému uživatelskému zážitku a bezpečnostním rizikům.

Před standardizací BGF používali operátoři různé proprietární hraniční řadiče relací s nekonzistentními implementacemi, které bránily interoperabilitě mezi různými dodavateli a operátory. Tato fragmentace zvyšovala náklady a složitost nasazení a zároveň omezovala inovace služeb. Standardizovaná BGF od 3GPP poskytla jednotný přístup k hraniční kontrole médií, což umožnilo konzistentní vynucování politik, bezpečnostní ochranu a správu kvality napříč prostředími s více dodavateli a operátory. Konkrétně řešila omezení dřívějších přístupů integrací s řídicí rovinou IMS a politickým rámcem, což umožnilo dynamickou aplikaci politik na základě požadavků relací v reálném čase.

Vytvoření BGF bylo motivováno potřebou umožnit bezpečné a spolehlivé poskytování multimediálních služeb ve stále více propojeném světě, kde uživatelé očekávají bezproblémovou kvalitu služeb bez ohledu na hranice sítí. Řešila základní problémy včetně průchodu [NAT](/mobilnisite/slovnik/nat/) a firewallem pro mediální toky, ochrany před útoky typu denial-of-service zaměřenými na multimediální infrastrukturu a vynucování smluv o úrovni služeb pro kvalitu služeb. Poskytnutím standardizovaných rozhraní a schopností BGF snížila náklady operátorů a zároveň zlepšila kvalitu a bezpečnost služeb, což v konečném důsledku umožnilo rozšířené přijetí služeb založených na IMS, jako je VoLTE a videotelefonie.

## Klíčové vlastnosti

- Řízení a vynucování multimediálního provozu na základě politik
- Průchod Network Address Translation (NAT) a firewallem pro mediální toky
- Hluboká kontrola paketů pro klasifikaci médií a monitorování kvality
- Zabezpečení propojení včetně ochrany před DoS a validace médií
- Správa šířky pásma a vynucování kvality služeb
- Podpora zákonného odposlechu pro soulad s regulacemi

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)
- [NAT – Network Address Translation](/mobilnisite/slovnik/nat/)

## Definující specifikace

- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture
- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 29.421** (Rel-8) — IMS Interworking with External IP Networks

---

📖 **Anglický originál a plná specifikace:** [BGF na 3GPP Explorer](https://3gpp-explorer.com/glossary/bgf/)
