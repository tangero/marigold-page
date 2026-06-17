---
slug: "bir"
url: "/mobilnisite/slovnik/bir/"
type: "slovnik"
title: "BIR – BootstrappingInfo-Request message"
date: 2025-01-01
abbr: "BIR"
fullName: "BootstrappingInfo-Request message"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bir/"
summary: "Zpráva protokolu Diameter používaná v architektuře GAA (Generic Authentication Architecture) v 3GPP k vyžádání inicializačních informací od funkce BSF (Bootstrapping Server Function). Zahajuje proces"
---

BIR je zpráva protokolu Diameter používaná v architektuře GAA (3GPP) k vyžádání inicializačních informací od BSF, čímž zahajuje autentizaci a dohodu klíčů pro zabezpečený přístup ke službám.

## Popis

Zpráva BootstrappingInfo-Request (BIR) je klíčový příkaz protokolu Diameter v rámci architektury [GAA](/mobilnisite/slovnik/gaa/) (Generic Authentication Architecture) dle 3GPP, konkrétně definovaný ve specifikaci rozhraní Zh (TS 29.109). Slouží jako počáteční požadavek od síťové aplikační funkce ([NAF](/mobilnisite/slovnik/naf/)) směrem k funkci [BSF](/mobilnisite/slovnik/bsf/) (Bootstrapping Server Function) pro získání potřebných autentizačních vektorů a sdílených klíčů nutných pro zabezpečení komunikace s uživatelským zařízením (UE). Zpráva funguje v modelu klient-server, kde NAF vystupuje jako klient Diameter a BSF jako server, přičemž využívá základní protokol Diameter rozšířený o specifické atributy ([AVP](/mobilnisite/slovnik/avp/)) dle 3GPP pro přenos autentizačních informací.

Když se UE pokouší přistoupit ke službě poskytované NAF (například službě [MBMS](/mobilnisite/slovnik/mbms/) nebo zabezpečenému aplikačnímu serveru), nemusí mít NAF s UE přímé bezpečnostní spojení. Namísto implementace vlastního autentizačního mechanismu odešle NAF zprávu BIR k BSF. Tato zpráva obsahuje identifikátory jak pro UE (typicky [IMPI](/mobilnisite/slovnik/impi/) nebo [IMPU](/mobilnisite/slovnik/impu/)), tak pro žádající NAF (identifikátor NAF). BSF, která udržuje vztah důvěry s [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server) a již s UE předtím provedla inicializační proceduru pomocí protokolu AKA, tento požadavek zpracuje, aby ověřila, zda pro dané UE existuje platný bezpečnostní kontext.

Technická operace spočívá v tom, že zpráva BIR spustí v BSF vyhledání příslušné inicializační relace pro UE. Pokud platná relace existuje, BSF vygeneruje specifický klíč Ks_NAF, odvozený z hlavního relací klíče (Ks) sdíleného mezi UE a BSF, a identifikátoru NAF. Tento klíč je unikátní pro dvojici UE-NAF. BSF následně odpoví zprávou BootstrappingInfo-Answer (BIA) obsahující klíč Ks_NAF (nebo odkaz na něj) a přidruženou životnost klíče. NAF pak tento klíčový materiál použije k navázání zabezpečeného kanálu s UE, často pomocí protokolů jako HTTP Digest AKA nebo TLS-PSK. Tato architektura centralizuje správu autentizace v BSF, což umožňuje různorodým NAF využívat přihlašovací údaje z 3GPP předplatného, aniž by každá z nich potřebovala přímý přístup k HSS nebo implementovala složitou logiku AKA.

Struktura zprávy BIR zahrnuje povinné AVP, jako jsou Session-Id, Origin-Host, Origin-Realm, Destination-Host, Destination-Realm a Auth-Application-Id. Zásadně nese AVP User-Name obsahující soukromou identitu uživatele (IMPI) a AVP NAF-Id identifikující žádající aplikační funkci. Volitelné AVP mohou žádat o specifické typy klíčů nebo indikovat podporované bezpečnostní protokoly. Tento návrh umožňuje flexibilní integraci s různými servisními architekturami při zachování silné bezpečnosti odvozené z autentizační infrastruktury jádra sítě. Výměna BIR/BIA je zásadní pro umožnění schopností podobných jednotnému přihlašování napříč různými službami v sítích 3GPP.

## K čemu slouží

Zpráva BIR a širší architektura GAA byly vytvořeny k řešení problému zabezpečené autentizace služeb pro aplikace mimo tradiční okruhově a paketově přepínané domény 3GPP. Před GAA musela každá nová aplikační služba (jako streamování, hry nebo podnikový přístup) vyžadující autentizaci buď implementovat vlastní systém správy přihlašovacích údajů, nebo najít způsob přímého rozhraní se složitým HSS, což bylo nepraktické a nebezpečné. To vedlo k roztříštěné bezpečnosti, špatné uživatelské zkušenosti s více hesly a zvýšeným provozním nákladům pro poskytovatele služeb.

Primární motivací bylo využít silnou autentizaci sítí 3GPP založenou na SIM kartě (UMTS AKA) k zabezpečení širokého spektra služeb založených na IP. Zpráva BIR poskytuje standardizovaný mechanismus, pomocí kterého tyto externí služby (NAF) mohou žádat a získávat kryptografické klíče odvozené z autentizace jádra sítě, aniž by byly kdy odhaleny hlavní klíče nebo aby NAF musela rozumět protokolu AKA. Tím se řeší klíčová omezení: zabraňuje se množení přihlašovacích údajů, využívá se robustní zabezpečení SIM karty a umožňuje se bezproblémový uživatelský zážitek, kdy lze síťovou autentizaci znovu použít pro přístup ke službám.

Historicky zavedená ve 3GPP Release 6 a upřesňovaná v následujících vydáních, umožnila zpráva BIR nové obchodní modely pro mobilní operátory a poskytovatele služeb. Umožnila jim nabízet služby s přidanou hodnotou s vestavěným zabezpečením na úrovni operátora, což je konkurenční výhodou vůči internetovým poskytovatelům služeb. Architektura vyřešila technickou výzvu bezpečné distribuce relací klíčů od centrální autentizační autority (BSF) k potenciálně nedůvěryhodným nebo externím aplikačním serverům, což je základní požadavek pro éru mobilního internetu. Tvoří základ pro autentizaci v MBMS, přístupu k IMS aplikacím a dalších zabezpečených službách definovaných v pozdějších vydáních.

## Klíčové vlastnosti

- Zahajuje proceduru žádosti o klíč v architektuře GAA (Generic Authentication Architecture)
- Používá standardizovaný protokol Diameter přes referenční bod Zh
- Nese identitu uživatele (IMPI/IMPU) a identifikátor síťové aplikační funkce (NAF)
- Spouští odvození službě specifického sdíleného klíče Ks_NAF funkcí BSF (Bootstrapping Server Function)
- Umožňuje zabezpečenou autentizaci mezi uživatelským zařízením a externími aplikačními servery bez nutnosti samostatných přihlašovacích údajů
- Podporuje opakované využití autentizace 3GPP AKA pro přístup k ne-3GPP službám

## Definující specifikace

- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)

---

📖 **Anglický originál a plná specifikace:** [BIR na 3GPP Explorer](https://3gpp-explorer.com/glossary/bir/)
