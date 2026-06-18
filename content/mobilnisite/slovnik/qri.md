---
slug: "qri"
url: "/mobilnisite/slovnik/qri/"
type: "slovnik"
title: "QRI – QoS Rule Identifier"
date: 2025-01-01
abbr: "QRI"
fullName: "QoS Rule Identifier"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/qri/"
summary: "Jedinečný identifikátor přiřazený pravidlu QoS v systému 5G (5GS) pro řízení zacházení s toky paketů. Umožňuje síti a uživatelskému zařízení (UE) jednoznačně odkazovat na konkrétní pravidla QoS pro je"
---

QRI je jedinečný identifikátor přiřazený pravidlu QoS v rámci systému 5G, který umožňuje síti a uživatelskému zařízení (UE) jednoznačně odkazovat na konkrétní pravidla a vynucovat je pro dynamické zacházení s toky paketů.

## Popis

Identifikátor pravidla QoS (QRI) je základním prvkem modelu kvality služeb (QoS) v 5G definovaného od 3GPP Release 15. Pravidlo QoS je soubor parametrů, který definuje, jak má být se specifickým tokem služebních dat ([SDF](/mobilnisite/slovnik/sdf/)) nebo agregátem SDFů zacházeno z hlediska přeposílání paketů (např. priorita, rozpočet zpoždění paketů, míra chybovosti paketů). Každému pravidlu QoS nakonfigurovanému v uživatelském zařízení (UE) nebo uplatňovanému sítí je přiřazen jedinečný QRI. QRI je celočíselná hodnota, která slouží jako odkaz na konkrétní pravidlo v signalizaci a operacích souvisejících s QoS.

Z architektonického hlediska QRI funguje v kontextu relace [PDU](/mobilnisite/slovnik/pdu/). Během vytváření nebo modifikace relace PDU může funkce pro správu relací ([SMF](/mobilnisite/slovnik/smf/)) vytvářet pravidla QoS a přiřazovat jim QRIs. Tato pravidla spolu s jejich identifikátory jsou následně poskytnuta uživatelskému zařízení (UE) prostřednictvím protokolu [NAS](/mobilnisite/slovnik/nas/) [SM](/mobilnisite/slovnik/sm/) (specifikovaného v TS 24.501) a (R)ANu prostřednictvím rozhraní [N2](/mobilnisite/slovnik/n2/). Uživatelské zařízení (UE) používá QRI k mapování paketů uplink v uživatelské rovině na příslušný tok QoS (identifikovaný [QFI](/mobilnisite/slovnik/qfi/) - identifikátorem toku QoS) na základě filtrů paketů a priority definovaných v odpovídajícím pravidle QoS. Ve směru downlink označuje [UPF](/mobilnisite/slovnik/upf/) pakety pomocí QFI a (R)AN používá vazbu mezi QFI a profilem QoS (který je prostřednictvím QRI asociován s pravidly QoS) k aplikaci správného zacházení s rádiovými prostředky.

Princip fungování: Když se SMF rozhodne nainstalovat, upravit nebo odstranit pravidlo QoS pro relaci PDU, zahrne QRI do příslušných zpráv N1 (pro UE) a N2 (pro (R)AN). Například v příkazu pro modifikaci relace PDU může SMF odeslat operaci s pravidlem QoS (např. 'přidat') s novou hodnotou QRI. Uživatelské zařízení (UE) toto pravidlo uloží lokálně ve svém kontejneru pravidel QoS. Během přenosu v uplinku vyhodnocuje klasifikátor uplinku v uživatelském zařízení hlavičky paketů proti filtrům paketů všech pravidel QoS v pořadí podle priority. Když dojde k shodě, označí uživatelské zařízení (UE) paket QFI odpovídajícím QRI nalezeného pravidla (prostřednictvím vazby známé z pravidla QoS). To umožňuje konzistentní vynucování QoS na koncích. Úlohou QRI je tedy poskytovat stabilní referenční bod pro správu potenciálně dynamické sady pravidel QoS na relaci PDU, což umožňuje efektivní aktualizace bez nejednoznačností.

## K čemu slouží

QRI byl zaveden spolu s novým modelem QoS pro 5G v Release 15, aby odstranil omezení mechanismu QoS založeného na přenašečích v EPS (4G). V EPS byla QoS pevně svázána s přenašeči EPS a pravidla byla implicitně asociována s šablonou toku přenosů (TFT) přenašeče. To činilo dynamické úpravy QoS obtížnými, protože změna filtrů často vyžadovala modifikaci přenašeče. Systém 5G odděluje pravidla QoS od transportní vrstvy (toků QoS), což umožňuje flexibilnější a granulárnější řízení QoS. QRI existuje proto, aby v této oddělené architektuře jednoznačně identifikoval každé nezávislé pravidlo QoS.

Motivace vychází z potřeby podporovat rozmanité případy užití 5G – od rozšířeného mobilního širokopásmového připojení (eMBB) přes ultra-spolehlivé komunikace s nízkou latencí (URLLC) až po hromadný IoT – z nichž každý má odlišné požadavky na QoS. Byl potřeba systém, ve kterém by síť mohla rychle přidávat, upravovat nebo odstraňovat pravidla pro detekci a zacházení s pakety bez narušení probíhajících toků. QRI poskytuje potřebný odkaz pro takové operace. Řeší problém jednoznačné reference ve signalizaci: když SMF instruuje uživatelské zařízení (UE) k aktualizaci konkrétního pravidla, použije QRI k přesné identifikaci, které pravidlo změnit. To umožňuje jemně granulované, službou řízené řízení QoS, které je zásadní pro síťové segmenty (network slicing) a efektivní využití prostředků v servisně orientované architektuře 5G.

## Klíčové vlastnosti

- Jedinečný celočíselný identifikátor pro pravidlo QoS v rámci relace PDU
- Používá se v signalizaci N1 (UE) a N2 ((R)AN) k odkazování na konkrétní pravidla QoS
- Umožňuje dynamické přidávání, úpravy a odstraňování pravidel QoS
- Poskytuje vazbu mezi filtry paketů pravidla QoS a identifikátorem toku QoS (QFI)
- Zásadní pro oddělený model QoS v 5G, který odděluje pravidla od toků
- Podporuje granulární řízení QoS pro různé požadavky služeb 5G

## Definující specifikace

- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3

---

📖 **Anglický originál a plná specifikace:** [QRI na 3GPP Explorer](https://3gpp-explorer.com/glossary/qri/)
