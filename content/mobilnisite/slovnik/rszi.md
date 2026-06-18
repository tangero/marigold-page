---
slug: "rszi"
url: "/mobilnisite/slovnik/rszi/"
type: "slovnik"
title: "RSZI – Regional Subscription Zone Identity"
date: 2025-01-01
abbr: "RSZI"
fullName: "Regional Subscription Zone Identity"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rszi/"
summary: "RSZI je kód identifikující geografickou oblast, ve které je účastníkovi povoleno využívat služby, a umožňuje tak regionální kontrolu předplatného. Operátorům umožňuje omezit využívání služeb na konkré"
---

RSZI je kód identifikující geografickou oblast, ve které je účastníkovi povoleno využívat služby, což operátorům umožňuje regionální kontrolu předplatného.

## Popis

Regionální identifikátor zóny předplatného (Regional Subscription Zone Identity, RSZI) je síťový identifikátor definovaný ve specifikacích 3GPP pro vymezení konkrétních geografických oblastí za účelem kontroly předplatného. Funguje jako klíčový parametr v profilu účastníka uloženém v síťových entitách, jako je Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). RSZI není fyzický síťový prvek, ale logický identifikátor mapovaný na definovanou množinu lokalizačních oblastí, směrovacích oblastí nebo sledovacích oblastí v rámci pokrytí sítě. Když se uživatelské zařízení (User Equipment, UE) pokusí o přístup k síti, obsluhující síťový uzel (jako je Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/))) porovná polohu UE s povolenými RSZI v jeho profilu předplatného. Tato kontrola je základní součástí procedur správy mobility a řízení přístupu.

Z architektonického hlediska je RSZI integrován do rámců správy dat předplatného a autorizace přístupu. Základní síťové entity zodpovědné za data účastníka, jako je HLR v sítích GSM/UMTS nebo HSS v sítích LTE/5G, ukládají seznam autorizovaných RSZI pro každého účastníka. Během procedur aktualizace polohy nebo když UE zahájí spojení, navštívená síť poskytne informace o své aktuální poloze (např. Location Area Identity ([LAI](/mobilnisite/slovnik/lai/)), Routing Area Identity ([RAI](/mobilnisite/slovnik/rai/)) nebo Tracking Area Identity ([TAI](/mobilnisite/slovnik/tai/))). Obsluhující uzel nebo vyhrazené autentizační centrum porovná tento identifikátor polohy se seznamem povolených RSZI účastníka. Následně je vynuceno autorizační rozhodnutí – povolit nebo odepřít službu – což často spouští specifické účtovací události nebo v případě odepření přístupu nasměruje UE na příslušné oznámení o službě.

Její role v síti je primárně provozní a komerční. Z pohledu provozu sítě umožňuje RSZI přesnou geografickou kontrolu služeb, kterou lze využít pro plánování sítě, distribuci zátěže a správu služeb pro nouzové situace. Komerčně jde o technický nástroj pro regionální tarify předplatného, kde účastníci platí nižší sazby za služby omezené na 'domovskou zónu' a potenciálně vyšší sazby nebo žádnou službu mimo ni. Podporuje také regulatorní požadavky, jako jsou licenční podmínky omezující službu na určité regiony. Mechanismus RSZI zajišťuje, že síť může tato geografická omezení služeb účinně a spolehlivě vynucovat bez nutnosti neustálého manuálního zásahu, automatizuje řízení přístupu na základě dynamické polohy UE.

## K čemu slouží

RSZI bylo zavedeno, aby vyřešilo problém geografického omezení mobilních služeb předplatného, což je požadavek daný komerčními i regulatorními potřebami. Před existencí takových standardizovaných mechanismů bylo nabízení regionálně specifických tarifů nebo vynucování licencí pro servisní oblasti složité, často se spoléhalo na méně podrobné síťové filtrování nebo manuální provizionování, což bylo náchylné k chybám a obtížně škálovatelné. Operátoři hledali standardizovaný způsob, jak vytvářet tarify 'domovské zóny', které byly oblíbené pro přilákání zákazníků nižšími cenami za místní využití, zatímco za národní roaming se účtovaly prémiové sazby.

Historicky, jak se mobilní sítě rozšiřovaly a rostla konkurence, potřebovali operátoři flexibilnější nabídky služeb. Vytvoření RSZI poskytlo čistou metodu definování servisních zón založenou na profilu účastníka. Tím se vyřešilo omezení dřívějších, více síťově orientovaných přístupů, které nemusely přesně odpovídat hranicím komerčních tarifů. Propojením identity zóny přímo s předplatným mohli operátoři dynamicky spravovat servisní oblasti prostřednictvím backendových systémů bez nutnosti rekonfigurace každého radiového síťového řadiče nebo základnové stanice. Pro regulátory navíc poskytlo ověřitelný technický prostředek, jak zajistit, že operace držitele licence jsou omezeny na udělenou geografickou koncesi, což podporuje monitorování shody a správu spektra.

## Klíčové vlastnosti

- Logický identifikátor pro geografické servisní zóny
- Uložen v profilu účastníka (HLR/HSS)
- Používán v procedurách řízení přístupu a autorizace
- Umožňuje regionálně specifické tarify a účtování
- Podporuje dodržování regulatorních požadavků na servisní oblast
- Integrován s kontrolami správy mobility (LAI/RAI/TAI)

## Související pojmy

- [LAI – Location Area Identity](/mobilnisite/slovnik/lai/)
- [RAI – Routing Area Identity](/mobilnisite/slovnik/rai/)
- [TAI – Tracking Area Identifier](/mobilnisite/slovnik/tai/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [RSZI na 3GPP Explorer](https://3gpp-explorer.com/glossary/rszi/)
