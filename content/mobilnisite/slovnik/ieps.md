---
slug: "ieps"
url: "/mobilnisite/slovnik/ieps/"
type: "slovnik"
title: "IEPS – International Emergency Preference Scheme"
date: 2025-01-01
abbr: "IEPS"
fullName: "International Emergency Preference Scheme"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ieps/"
summary: "Síťová služba poskytující přednostní zacházení pro nouzovou komunikaci. Zajišťuje, aby hovory a zprávy od oprávněného nouzového personálu nebo uživatelů v krizových situacích získaly vyšší prioritu ne"
---

IEPS je síťová služba, která poskytuje přednostní zacházení pro nouzovou komunikaci a zajišťuje, aby oprávněný personál a uživatelé v krizových scénářích získali vyšší prioritu oproti běžnému provozu při zahlcení sítě.

## Popis

International Emergency Preference Scheme (IEPS) je služební funkce standardizovaná organizací 3GPP pro správu telekomunikačních prostředků během mimořádných událostí, katastrof nebo období silného zahlcení sítě. Funguje tak, že přiřazuje vyšší úroveň priority určené komunikaci, která může zahrnovat hlasové hovory, SMS a paketové datové relace iniciované oprávněnými uživateli nebo subjekty. Mezi tyto oprávněné uživatele typicky patří vládní záchranné složky (např. policie, hasiči, zdravotnická služba), organizace pro pomoc při katastrofách a případně poskytovatelé základních služeb. Schéma funguje pomocí kombinace předplatitelských dat v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) uživatele, signalizačních příznaků ve zprávách pro sestavení hovoru/relace a vymáhacích mechanismů v jádrové a rádiové síti.

Z architektonického hlediska se IEPS týká více síťových uzlů. Profil předplatitele pro oprávněného uživatele obsahuje indikátor IEPS. Když takový uživatel zahájí hovor nebo relaci, obslužná funkce Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) v IMS nebo Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) v sítích s přepojováním okruhů identifikuje předplatné IEPS. Poté označí odpovídající zprávu Session Initiation Protocol (SIP) INVITE nebo [ISUP](/mobilnisite/slovnik/isup/) [IAM](/mobilnisite/slovnik/iam/) specifickými indikátory priority, jako je hlavička Priority v SIP nebo parametry Precedence and Preemption (P&P). Tyto značky se šíří sítí. V rádiové přístupové síti (RAN) základnová stanice (eNodeB/gNodeB) tyto indikátory používá během sestavování spojení Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) a plánování. Provoz IEPS může získat přidělené prostředky před provozem s běžnou prioritou (best-effort) a může dokonce přednostně ukončit probíhající spojení s nižší prioritou, pokud jsou prostředky zcela nedostatečné, a to podle definovaných pravidel přednostního ukončení.

Jeho úlohou je zajistit, aby se zásadní komunikace neblokovala během krizí, kdy veřejné sítě zažívají extrémní zatížení nebo částečné poškození. Toto schéma je nedílnou součástí telekomunikací pro národní bezpečnost a ochranu veřejnosti. Funguje end-to-end, potenciálně přes administrativní a mezinárodní hranice, za předpokladu, že roamingové dohody podporují IEPS. Specifikace podrobně popisují protokoly pro předávání priority IEPS, chování síťových prvků při přijetí takových značek a postupy správy pro autorizaci uživatelů. IEPS je klíčovým prvkem pro služby Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)) v sítích 3GPP, který zajišťuje, že záchranné složky mohou komunikovat, když to nejvíce záleží.

## K čemu slouží

IEPS byl vytvořen, aby řešil kritické selhání veřejných mobilních sítí během hromadných mimořádných událostí, jako jsou přírodní katastrofy nebo teroristické útoky, kdy zahlcení sítě z běžného využití může zcela blokovat hovory od záchranných složek. Tradiční mobilní služby fungují na principu prvního příchodu nebo s běžnou prioritou (best-effort), což je pro krizové řízení nedostatečné. Toto schéma problém řeší zavedením řízeného rámce priority.

Motivace vychází z poučení získaných z minulých katastrof a z požadavků orgánů ochrany veřejnosti využít komerční mobilní sítě pro nákladově efektivní pokrytí široké oblasti, které doplňuje nebo nahrazuje vyhrazené systémy pozemní mobilní radiokomunikace (LMR). IEPS poskytuje standardizovanou schopnost "prosazení se", kterou tyto orgány požadují. Řeší omezení dřívějších, proprietárních nebo pouze národních prioritních služeb vytvořením mezinárodně uznávaného a interoperabilního standardu. To umožňuje například zahraničnímu týmu pro pomoc při katastrofách, aby jejich komunikace měla při roamingu v zemi postižené katastrofou prioritu.

Historicky existovaly prioritní telefonní služby v armádních a vládních sítích. IEPS přináší tuto koncepci do globálního ekosystému 3GPP, formalizuje ji ve verzi Rel-2 a vylepšuje v pozdějších vydáních tak, aby pokrývala vyvíjející se síťové architektury, jako jsou IMS a 5G. Řeší problém zajištění spolehlivé nouzové komunikace ve sdílené veřejné infrastruktuře, což je základním kamenem moderního plánování odolnosti vůči katastrofám.

## Klíčové vlastnosti

- Poskytuje přednostní označování komunikace oprávněných uživatelů na základě předplatného.
- Umožňuje end-to-end přednostní zpracování napříč doménami s přepojováním okruhů, IMS a paketovými sítěmi.
- Podporuje přednostní ukončení probíhajících relací s nižší prioritou, aby se uvolnily prostředky pro nouzový provoz.
- Definuje standardizované signalizační parametry (např. hlavičku Priority v SIP, hodnoty ARP) pro interoperabilitu.
- Zahrnuje správní funkce pro autorizaci a administraci seznamů uživatelů IEPS.
- Funguje ve spojení s Access Class Barring a dalšími mechanismy řízení zahlcení.

## Definující specifikace

- **TR 22.952** (Rel-19) — Priority Service Guide for 3GPP Networks
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [IEPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ieps/)
