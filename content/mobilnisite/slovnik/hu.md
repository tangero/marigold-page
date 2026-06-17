---
slug: "hu"
url: "/mobilnisite/slovnik/hu/"
type: "slovnik"
title: "HU – Home Units"
date: 2025-01-01
abbr: "HU"
fullName: "Home Units"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hu/"
summary: "Home Units (HU, domovské jednotky) označují primární nebo domovské síťové zařízení uživatele či kontext jeho předplatného. Jde o obecnou kategorizaci používanou ve specifikacích k odlišení entit nálež"
---

HU je obecná kategorizace 3GPP pro primární síťové zařízení uživatele nebo kontext jeho předplatného, která jej odlišuje od entit ve navštívených nebo poskytujících sítích.

## Popis

Home Units (HU, domovské jednotky) je konceptuální a kategorický termín používaný v technických specifikacích 3GPP k označení entit, zařízení nebo profilů předplatného, které jsou asociovány s primární nebo domovskou sítí uživatele. Slouží jako označení pro rozlišení mezi domovskou administrativní doménou a jinými doménami, jako jsou navštívené nebo poskytující sítě, zejména ve scénářích zahrnujících roamování. Samotný termín se často používá v klauzulích požadavků, architektonických popisech a kontextech testování spíše než pro pojmenování konkrétního protokolu nebo síťového uzlu.

V praxi může HU zahrnovat řadu konceptů. Může odkazovat na Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)), který uchovává hlavní data předplatného. Může také reprezentovat funkce řízení politik domovské sítě, jako je Home Policy Control Function ([H-PCF](/mobilnisite/slovnik/h-pcf/)) v raných architekturách, nebo profil předplatného uživatele uložený v Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) v 5G. Klíčovým principem je, že HU ztělesňuje autoritativní zdroj informací o účastníkovi a politik domovské sítě. Když uživatel roamuje, entity poskytující sítě ve Visited Network (VN) budou komunikovat s HU v Home Network ([HN](/mobilnisite/slovnik/hn/)) za účelem autentizace uživatele, získání dat předplatného a aplikace politik domovské sítě.

Role HU je zásadní pro mobilitu, roamování a konzistentní poskytování služeb. Zajišťuje, že bez ohledu na fyzickou polohu uživatele nebo rádiovou přístupovou síť, ke které je připojen, je jeho uživatelský zážitek řízen pravidly a daty od jeho domovského síťového poskytovatele. Toto oddělení odpovědností mezi domovskou a navštívenou sítí je základním kamenem globální buněčné interoperability. Z architektonického hlediska jsou interakce s HU definovány prostřednictvím standardizovaných rozhraní, jako jsou rozhraní založená na Diameter mezi navštíveným [MME](/mobilnisite/slovnik/mme/) a domovským HSS, nebo servisně orientovaná rozhraní v 5G Core.

## K čemu slouží

Koncept Home Units existuje, aby formálně oddělil administrativní a funkční odpovědnosti mezi poskytovatelem domovské sítě účastníka a jakoukoli jinou sítí, kterou účastník může dočasně používat. Toto oddělení je nezbytné pro umožnění globálního roamování, kdy uživatel může získávat služby ze sítě provozované jiným poskytovatelem. Bez jasné definice 'domovské' entity by správa dat účastníka, autentizace, účtování a vynucování politik přes síťové hranice byla chaotická a neinteroperabilní.

Historicky, jak se buněčné sítě vyvíjely z nasazení jediného operátora ke komplexním mezinárodním federacím, byl potřeba standardizovaný model. Koncept HU řeší omezení monolitických síťových architektur definováním jasného 'domovského' kotvícího bodu. Řeší problémy související se správou identity účastníka, přenositelností služeb a konzistentní aplikací politik. Domovská síť si ponechává kontrolu nad hlavním záznamem předplatného a klíčovými politikami, zatímco navštívená síť poskytuje rádiový přístup a lokální směrování. Tento model motivoval vytvoření jasných rozhraní (jako Cx/Dx, S6a, N8/N10) a protokolů speciálně navržených pro komunikaci mezi funkcemi poskytující sítě a domovskými jednotkami, což zajišťuje bezpečnost a spolehlivost operací přes sítě.

## Klíčové vlastnosti

- Reprezentuje autoritativní doménu domovské sítě pro účastníka
- Uchovává hlavní data předplatného a trvalé identity účastníka
- Kotví politiky domovské sítě a pravidla účtování
- Nezbytné pro autentizaci a autorizaci v roamovacích scénářích
- Poskytuje konzistentní referenční bod pro poskytování služeb
- Odlišeno od Visited Units (VU) nebo entit Poskytující sítě

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [HU na 3GPP Explorer](https://3gpp-explorer.com/glossary/hu/)
