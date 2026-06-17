---
slug: "lcaf"
url: "/mobilnisite/slovnik/lcaf/"
type: "slovnik"
title: "LCAF – Location Client Authorization Function"
date: 2025-01-01
abbr: "LCAF"
fullName: "Location Client Authorization Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lcaf/"
summary: "Síťová funkce v architektuře lokalizačních služeb (LCS), která autorizuje žádosti od externích či interních klientů o získání polohy mobilního zařízení. Ověřuje identitu klienta a kontroluje, zda má o"
---

LCAF (Location Client Authorization Function) je funkce lokalizačních služeb (Location Services), která autorizuje požadavky klientů na určení polohy mobilního zařízení ověřením identity klienta a kontrolou oprávnění za účelem vynucení pravidel ochrany soukromí a bezpečnostních politik.

## Popis

Location Client Authorization Function (LCAF) je klíčová logická komponenta v architektuře lokalizačních služeb ([LCS](/mobilnisite/slovnik/lcs/)) dle 3GPP, původně definovaná pro GSM a vyvíjená pro UMTS a LTE/5G. Jejím hlavním úkolem je fungovat jako vrátný pro lokalizační požadavky. Když klient lokalizačních služeb (LCS Client, kterým může být externí aplikace, poskytovatel služeb s přidanou hodnotou nebo interní síťová služba) odešle žádost o určení polohy mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) nebo uživatelského zařízení (UE), je tato žádost směrována k LCAF. LCAF provede autorizaci ověřením přihlašovacích údajů klienta a porovnáním žádosti s profilem ochrany soukromí cílového účastníka. Profil ochrany soukromí účastníka, který je často spravován samostatnou funkcí jako Location Client Privacy Function (LCPF) nebo [GMLC](/mobilnisite/slovnik/gmlc/), definuje, kdo je oprávněn žádat o polohu účastníka a za jakých podmínek (např. pouze v nouzových případech, pouze konkrétní klienti, časová omezení).

Z provozního hlediska LCAF komunikuje s Gateway Mobile Location Centre (GMLC), které je hlavním vstupním bodem pro externí lokalizační požadavky. LCAF může být umístěna společně s GMLC nebo implementována jako samostatná entita. Po přijetí lokalizační žádosti LCAF ověří klienta LCS pomocí identifikátorů, jako je ID klienta a heslo, nebo v pozdějších vydáních pokročilejších certifikátů. Následně získá nastavení ochrany soukromí cílového účastníka z Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Na základě této kontroly LCAF žádost buď schválí, zamítne, nebo může uplatnit konkrétní omezení (např. poskytnout pouze přibližnou polohu). Pokud je žádost autorizována, je předána příslušným síťovým prvkům (např. [MSC](/mobilnisite/slovnik/msc/), SGSN, [MME](/mobilnisite/slovnik/mme/) nebo [AMF](/mobilnisite/slovnik/amf/)), aby byla zahájena procedura určení polohy s rádiovým přístupovým sítí.

LCAF je nezbytná pro soulad s právními a regulačními požadavky na ochranu soukromí uživatelů, jako je například GDPR EU nebo regionální telekomunikační předpisy. Zajišťuje, že poloha uživatele – vysoce citlivá osobní informace – nebude zveřejněna bez řádného souhlasu nebo zákonného zmocnění. Ve vyvinuté architektuře pro 5G jsou lokalizační služby definovány v kontextu architektury založené na službách (SBA), kde Network Exposure Function (NEF) často funguje jako brána pro externí aplikace. Principy autorizace LCAF jsou začleněny do schopností NEF, kde NEF ověřuje a autorizuje aplikační funkce (AF) žádající o informace o poloze a kontroluje politiky uložené v Unified Data Repository (UDR). Tento vývoj zachovává základní princip LCAF, tj. autorizaci klienta, v rámci moderního cloudového nativního rámce.

## K čemu slouží

LCAF byla vytvořena k řešení základních výzev v oblasti ochrany soukromí a bezpečnosti, které jsou neodmyslitelné při poskytování síťových lokalizačních služeb. Když mobilní operátoři začali nasazovat služby jako E-911 v USA nebo podobné nouzové služby jinde, potřebovali mechanismus, který by umožňoval autorizovaným záchranným službám lokalizovat volající, ale zároveň bránil neoprávněnému sledování jinými subjekty. Nad rámec nouzových služeb se objevily komerční služby založené na poloze (LBS), jako je správa vozového parku, aplikace pro vyhledání přátel nebo cílená reklama, což vytvořilo potřebu standardizovaného způsobu správy přístupu klientů. Bez LCAF by neexistovala standardizovaná, bezpečná metoda kontroly toho, kteří klienti mohou žádat o data o poloze, což by vedlo k možným porušením soukromí a nedodržování předpisů.

Její zavedení, sahající až do období GSM (R99), vyřešilo problém, jak síťovou lokalizační schopnost kontrolovaně zpřístupnit třetím stranám. Předchozí neformální metody byly nejisté a neškálovatelné. LCAF vytvořila formalizovanou autorizační vrstvu, která odděluje požadavek klienta od samotné technologie určování polohy. To umožňuje operátorům vynucovat preference účastníků týkající se ochrany soukromí (opt-in/opt-out), plnit požadavky na zákonné odposlechy a vytvářet komerční rámce pro LCS. Umožnila růst celého ekosystému LBS tím, že poskytla důvěryhodné, standardizované rozhraní, které účastníkům zaručovalo, že jejich data o poloze budou chráněna v souladu s jejich přáními a zákonem.

## Klíčové vlastnosti

- Ověřuje klienty lokalizačních služeb (LCS Clients) pomocí standardizovaných přihlašovacích údajů
- Vyhodnocuje žádosti vůči profilům ochrany soukromí účastníka z HLR/HSS
- Vynucuje autorizační politiky pro lokalizační služby
- Může být integrována s Gateway Mobile Location Centre (GMLC)
- Podporuje rozlišení mezi nouzovými klienty, klienty služeb s přidanou hodnotou a interními klienty
- Poskytuje výsledek autorizace (schválení, zamítnutí, omezení) lokalizačnímu systému LCS

## Související pojmy

- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [LCAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lcaf/)
