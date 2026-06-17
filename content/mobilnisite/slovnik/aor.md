---
slug: "aor"
url: "/mobilnisite/slovnik/aor/"
type: "slovnik"
title: "AOR – Address Of Record"
date: 2025-01-01
abbr: "AOR"
fullName: "Address Of Record"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aor/"
summary: "AOR je SIP URI sloužící jako trvalá, veřejná identifikace uživatele v sítích IMS. Jednoznačně identifikuje účastníka pro účely registrace, směrování a vyvolávání služeb. Tento identifikátor je klíčový"
---

AOR je trvalá, veřejná identifikace uživatele v síti IMS ve formě SIP URI, používaná pro registraci, směrování a vyvolávání služeb.

## Popis

Address Of Record (AOR) je základní identifikátor v architektuře IP multimediálního subsystému (IMS) dle 3GPP, definovaný jako identifikátor URI (Uniform Resource Identifier) protokolu SIP (Session Initiation Protocol), který reprezentuje veřejnou identitu uživatele. Na rozdíl od dočasných kontaktních adres, které se mění s místem připojení k síti, slouží AOR jako stabilní, globálně směrovatelný identifikátor, který zůstává konstantní bez ohledu na aktuální polohu nebo zařízení uživatele. Tento trvalý identifikátor je uložen v [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server) jako součást profilu služeb uživatele a používají jej různé síťové prvky IMS pro směrování signalizačních zpráv, správu registrací a vyvolávání služeb.

Architektonicky funguje AOR jako primární klíč v procesu registrace do IMS. Když se uživatel registruje do sítě IMS, S-CSCF (Serving-Call Session Control Function) obdrží AOR od uživatelského zařízení (UE) a ověří jej proti databázi HSS. Po úspěšném ověření vytvoří S-CSCF vazbu mezi AOR a aktuální kontaktní adresou uživatele (typicky SIP URI obsahující IP adresu uživatelského zařízení). Tato vazba umožňuje síti IMS směrovat příchozí relace na správný cíl, i když se uživatel pohybuje mezi sítěmi nebo mění zařízení.

AOR se řídí specifickými pravidly formátování definovanými ve specifikacích 3GPP a standardech RFC. Obvykle má formát 'sip:uzivatel@domena' nebo 'sips:uzivatel@domena' pro zabezpečená připojení, kde část domény identifikuje domovskou síť uživatele. Uživatelská část může obsahovat různé identifikátory včetně telefonních čísel (ve formátu E.164 s konverzí na 'tel:' URI), adres ve stylu e-mailu nebo jiných jedinečných identifikátorů. Doménová složka AOR je klíčová pro rozhodování o směrování, protože určuje, která síť IMS by měla zpracovat počáteční požadavek prostřednictvím procedur založených na [DNS](/mobilnisite/slovnik/dns/).

V provozu umožňuje AOR několik kritických funkcí IMS nad rámec základní registrace. Slouží jako klíč pro získání profilu služeb z HSS, což umožňuje S-CSCF aplikovat příslušnou servisní logiku prostřednictvím interakce s aplikačními servery (Application Servers). AOR také podporuje funkce správy identit, jako jsou sady implicitní registrace, kde registrace jedné veřejné identity automaticky zaregistruje další přidružené identity. Dále tvoří základ pro mechanismy ochrany soukromí, protože uživatelé si mohou na základě nastavení v profilu služeb zvolit, zda svůj AOR během komunikace odhalí, či skryjí.

Role AOR se rozprostírá po celý životní cyklus relace. Při navazování relace se AOR objevuje v hlavičkách SIP, jako jsou From, To a Request-URI, což umožňuje správné směrování a vyvolávání služeb. Také podporuje scénáře větvení (forking), kde jeden AOR může být asociován s více koncovými body, což umožňuje současné zvonění na různých zařízeních. Oddělení trvalého AOR od dočasných kontaktních adres tvoří základ pro správu mobility v IMS a umožňuje bezproblémovou kontinuitu služeb při pohybu uživatelů mezi přístupovými sítěmi.

## K čemu slouží

Address Of Record (AOR) byl vytvořen, aby řešil základní problémy identifikace a směrování v IP multimediálních sítích. Před IMS se telekomunikační sítě spoléhaly na identifikátory z okruhově přepínaných sítí, jako je [MSISDN](/mobilnisite/slovnik/msisdn/) (Mobile Station International Subscriber Directory Number), které byly pevně svázány s konkrétními síťovými technologiemi a postrádaly flexibilitu potřebnou pro konvergované IP služby. Tyto starší identifikátory nemohly adekvátně podporovat bohaté multimediální služby, scénáře s více zařízeními a aplikace ve stylu internetu, které 3GPP předpokládalo pro budoucí sítě.

AOR řeší několik klíčových omezení tradičních telekomunikačních identifikátorů. Za prvé poskytuje technologickou nezávislost použitím SIP URI, které fungují napříč jakoukoli IP přístupovou sítí, což umožňuje skutečnou konvergenci mezi buněčnými, pevnými a WiFi sítěmi. Za druhé odděluje trvalou identitu uživatele od dočasných bodů připojení k síti, čímž řeší problém mobility, kdy uživatelé často mění IP adresy. Za třetí umožňuje bohaté vyvolávání služeb prostřednictvím asociace s uživatelskými profily v [HSS](/mobilnisite/slovnik/hss/), což dovoluje personalizované služby bez ohledu na způsob přístupu nebo typ zařízení.

Historicky koncept AOR vznikl ve standardech SIP od [IETF](/mobilnisite/slovnik/ietf/), kde byl definován jako trvalá adresa uživatele. 3GPP tento koncept v rámci architektury IMS přijalo a rozšířilo, aby vytvořilo jednotný identifikační rámec schopný podporovat jak tradiční telefonii, tak inovativní multimediální služby. Návrh AOR specificky řeší požadavky plně IP sítí, kde uživatelé mohou mít více zařízení, používat různé přístupové technologie a vyžadovat konzistentní zážitek ze služeb ve všech scénářích. Tím, že poskytuje stabilní kotvu v dynamickém IP prostředí, AOR umožňuje kontinuitu služeb, osobní mobilitu a flexibilní doručování služeb, které definují moderní komunikace založené na IMS.

## Klíčové vlastnosti

- Trvalý identifikátor typu SIP URI pro uživatele IMS
- Globálně směrovatelný napříč sítěmi IMS
- Odděluje identitu uživatele od bodů připojení k síti
- Umožňuje registraci a správu vazeb v S-CSCF
- Podporuje implicitní registraci více identit
- Tvoří základ pro získání profilu služeb a jejich vyvolání

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 24.525** (Rel-19) — Business Trunking Architecture & Requirements

---

📖 **Anglický originál a plná specifikace:** [AOR na 3GPP Explorer](https://3gpp-explorer.com/glossary/aor/)
