---
slug: "5g-eir"
url: "/mobilnisite/slovnik/5g-eir/"
type: "slovnik"
title: "5G-EIR – 5G Equipment Identity Register"
date: 2026-01-01
abbr: "5G-EIR"
fullName: "5G Equipment Identity Register"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/5g-eir/"
summary: "5G-EIR je síťová funkce, která ověřuje stav mobilních zařízení (UE) kontrolou jejich mezinárodního identifikátoru mobilního zařízení (IMEI) vůči černým, šedým a bílým listinám. Zabraňuje přístupu ukra"
---

5G-EIR je síťová funkce, která ověřuje mobilní zařízení kontrolou jejich IMEI vůči stavovým seznamům, aby zabránila přístupu ukradených, podvodných nebo nevyhovujících zařízení do sítě 5G.

## Popis

Registr identit zařízení pro 5G (5G-EIR) je klíčová bezpečnostní funkce v síti jádra 5G (5GC), která funguje jako samostatná síťová funkce ([NF](/mobilnisite/slovnik/nf/)) poskytující služby kontroly identity zařízení. Jejím hlavním úkolem je ověřit legitimitu a stav uživatelského zařízení (UE), které se pokouší připojit k síti, validací jeho mezinárodního identifikátoru mobilního zařízení ([IMEI](/mobilnisite/slovnik/imei/)) nebo IMEI s verzí softwaru ([IMEISV](/mobilnisite/slovnik/imeisv/)). 5G-EIR spravuje a dotazuje několik databází: černou listinu pro ukradená nebo zakázaná zařízení, šedou listinu pro zařízení pod dohledem a bílou listinu pro známá legitimní zařízení. Toto ověření je klíčovým krokem v řízení přístupu k síti a zajišťuje, že pouze autorizovaný a vyhovující hardware může využívat síťové služby.

Z architektonického hlediska je 5G-EIR navržen jako komponenta založená na službách v rámci architektury založené na službách ([SBA](/mobilnisite/slovnik/sba/)) 5GC. Vystavuje službu N5g-eir_EquipmentIdentityCheck ostatním autorizovaným síťovým funkcím, primárně funkci pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)). AMF funguje jako konzument služby a vyvolává službu 5G-EIR během počátečních registračních procedur nebo periodicky k ověření identity zařízení UE. Komunikace mezi AMF a 5G-EIR využívá standardizované rozhraní založené na službách, přičemž zprávy jsou přenášeny přes [HTTP](/mobilnisite/slovnik/http/)/2 s [JSON](/mobilnisite/slovnik/json/) datovou částí podle definice v 3GPP TS 29.511. Samotný 5G-EIR se může připojovat k externím databázím, jako je centrální globální databáze IMEI, aby obohatil své lokální rozhodování širšími průmyslovými údaji o stavu zařízení.

Základní operace zahrnuje odeslání zprávy požadavku na kontrolu identity zařízení (EquipmentIdentityCheck) z AMF do 5G-EIR. Tento požadavek obsahuje IMEI([SV](/mobilnisite/slovnik/sv/)) UE a případně další relevantní informace. 5G-EIR tento požadavek zpracuje kontrolou poskytnuté identity vůči svým interním seznamům. Následně vrátí odpověď udávající stav zařízení, typicky s hodnotami jako „WHITELISTED“, „BLACKLISTED“, „GREYLISTED“ nebo „UNKNOWN“. Na základě této odpovědi se AMF může rozhodnout, zda registraci povolí, zamítne, nebo uplatní specifická omezení. Pro zařízení na černé listině AMF typicky registraci zcela zamítne. Funkce 5G-EIR je bezstavová s ohledem na relaci UE; provádí čisté ověření identity, přičemž správu relace a vynucování ponechává na AMF.

Nad rámec základní kontroly seznamů hraje 5G-EIR zásadní roli při zmírňování podvodů založených na zařízeních a ochraně integrity sítě. Pomáhá operátorům bojovat proti používání padělaných zařízení, blokovat zařízení spojená s trvalou škodlivou činností a vynucovat regulatorní požadavky týkající se schválených typů zařízení. Díky integraci s architekturou SBA 5G nabízí 5G-EIR škálovatelnou, cloud-nativní bezpečnostní službu, kterou lze nasadit nezávisle a která je na vyžádání přístupná různým konzumentům NF, čímž se přizpůsobuje celkovým principům návrhu 5G, jako je modularita a síťové segmenty (network slicing). Její činnost je klíčová pro udržení důvěry v mobilní ekosystém tím, že zajišťuje legitimitu podkladového hardwaru připojujícího se k síti.

## K čemu slouží

5G-EIR existuje za účelem poskytování robustního ověřování identity zařízení v sítích 5G, čímž řeší kritickou potřebu zabránit neautorizovaným, ukradeným nebo vadným mobilním zařízením v přístupu k síťovým zdrojům. Jeho vytvoření bylo motivováno dlouhodobým problémem krádeží mobilních zařízení a podvodů, stejně jako potřebou zajistit soulad zařízení se síťovými standardy a regulatorními nařízeními. Kontrolou IMEI – jedinečného identifikátoru vestavěného do hardwaru zařízení – nabízí 5G-EIR bezpečnostní kontrolu na hardwarové úrovni, která doplňuje autentizaci účastníka (která ověřuje SIM kartu). Tím řeší problém, kdy by platná SIM karta mohla být použita v ukradeném nebo nevyhovujícím zařízení.

Historicky bylo ověřování identity zařízení prováděno funkcí EIR v sítích 2G, 3G a 4G. Tyto funkce však byly často monolitické síťové prvky s proprietárními rozhraními. Přechod na 5G představoval příležitost přearchitekturovat tuto funkci tak, aby odpovídala moderním cloud-nativním principům. Účelem 5G-EIR není pouze pokračovat v poskytování základní služby černé/bílé listiny, ale činit tak jako škálovatelnou webovou službu v rámci architektury založené na službách jádra 5G. Tím se řeší omezení minulosti, jako jsou omezení škálovatelnosti a složitá integrace, protože se z EIR stala standardizovaná NF, kterou lze snadno nasadit, škálovat a kterou mohou ostatní síťové funkce konzumovat prostřednictvím RESTful API.

Dále 5G-EIR podporuje zvýšené bezpečnostní požadavky 5G, včetně požadavků pro síťové segmenty (network slicing) a IoT. Pro síťové segmenty sloužící kritické infrastruktuře (např. průmyslové IoT, veřejná bezpečnost) mohou operátoři prostřednictvím 5G-EIR vynucovat přísnější politiky pro zařízení a zajistit, že pouze zařízení se specifickými, důvěryhodnými IMEI mají přístup k těmto segmentům. Pro masivní nasazení IoT může pomoci identifikovat a blokovat zařízení se známými zranitelnostmi nebo špatnými charakteristikami rádiového výkonu. Účel 5G-EIR se tedy rozšiřuje nad rámec protikrádežové ochrany a stává se základním nástrojem pro celkovou hygienu síťové bezpečnosti, správu souladu zařízení a ochranu specializovaných síťových služeb.

## Klíčové vlastnosti

- Validace IMEI(SV) vůči databázím černé, šedé a bílé listiny
- Rozhraní založené na službách (N5g-eir_EquipmentIdentityCheck) pro integraci s NF 5GC, jako je AMF
- Bezstavové ověření zařízení nezávislé na kontextu relace UE
- Podpora integrace s externími, globálními systémy databází IMEI
- Cloud-nativní návrh umožňující nezávislé škálování a nasazení
- Poskytuje výsledky stavu zařízení (např. BLACKLISTED, WHITELISTED) pro rozhodování AMF o registraci

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [IMEI – International Mobile Station Equipment Identities](/mobilnisite/slovnik/imei/)
- [UE – User Equipment](/mobilnisite/slovnik/ue/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 29.511** (Rel-19) — 5G Equipment Identity Register Service Interface

---

📖 **Anglický originál a plná specifikace:** [5G-EIR na 3GPP Explorer](https://3gpp-explorer.com/glossary/5g-eir/)
