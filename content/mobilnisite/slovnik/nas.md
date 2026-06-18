---
slug: "nas"
url: "/mobilnisite/slovnik/nas/"
type: "slovnik"
title: "NAS – Non-Access Stratum"
date: 2026-01-01
abbr: "NAS"
fullName: "Non-Access Stratum"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nas/"
summary: "NAS je funkční vrstva v protokolovém zásobníku mezi UE a jádrem sítě (MME/AMF). Zpracovává signalizaci pro správu mobility, správu relací a správu identity účastníka nezávisle na podkladové technologi"
---

NAS je protokolová vrstva mezi zařízením a jádrem sítě, která nezávisle spravuje mobilitu, relace a identitu účastníka za účelem navázání a udržení konektivity.

## Popis

Non-Access Stratum (NAS) je klíčová protokolová vrstva v řídicí rovině systémů 3GPP, která funguje přímo mezi uživatelským zařízením (UE) a řídicími uzly jádra sítě – konkrétně Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v 4G EPC a Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G Core. Leží nad Access Stratum ([AS](/mobilnisite/slovnik/as/)), které zpracovává rádiově specifickou signalizaci mezi UE a rádiovou přístupovou sítí (např. [eNB](/mobilnisite/slovnik/enb/), gNB). Toto rozvrstvení umožňuje, aby postupy NAS byly z velké části nezávislé na konkrétní rádiové technologii (např. LTE, NR, ne-3GPP přístup), což umožňuje konzistentní poskytování služeb jádra sítě napříč heterogenními přístupovými sítěmi. Protokol NAS je zodpovědný za nejkritičtější řídicí signalizaci související s registrací UE a jeho dosažitelností v rámci sítě.

Funkcionalita NAS je rozdělena do dvou primárních protokolových entit: entity Mobility Management ([MM](/mobilnisite/slovnik/mm/)) a entity Session Management ([SM](/mobilnisite/slovnik/sm/)). V EPS (4G) se jedná o protokoly EPS Mobility Management ([EMM](/mobilnisite/slovnik/emm/)) a EPS Session Management ([ESM](/mobilnisite/slovnik/esm/)). V 5GS jde o protokoly 5G Mobility Management (5GMM) a 5G Session Management (5GSM). Entita MM zpracovává postupy jako připojení/odpojení, aktualizace oblasti sledování, autentizaci a řízení bezpečnostního režimu. Spravuje registrační stav UE a zajišťuje, že síť může UE lokalizovat a vyvolat. Entita SM zpracovává zřizování, modifikaci a uvolňování paketových datových jednotek (PDU) relací neboli přenosových kanálů (bearerů), které představují datové kanály pro uživatelský provoz. Vyjednává parametry kvality služeb (QoS) a spravuje životní cyklus těchto datových kontextů.

Zprávy NAS jsou přenášeny přístupovou vrstvou (AS) transparentně. Když UE odešle zprávu NAS (např. Attach Request), je zapouzdřena protokoly AS (RRC v LTE/NR) a transportována k základnové stanici (eNB/gNB). Základnová stanice zprávu NAS extrahuje a přepošle ji příslušnému uzlu jádra sítě přes rozhraní S1-AP nebo NG-AP bez interpretace jejího obsahu. Tím je zajištěno jasné oddělení odpovědností: RAN spravuje rádiové zdroje, zatímco CN spravuje účastníka a relace. Signalizace NAS je vždy chráněna integritou a u citlivých zpráv je šifrována pomocí klíčů vytvořených během autentizace a dohody o klíči (AKA). Tato koncová bezpečnost mezi UE a jádrem sítě je základním kamenem bezpečnosti systémů 3GPP.

V průběhu jednotlivých releasů se NAS vyvíjel, aby podporoval stále širší škálu služeb a síťových architektur. Zavedl podporu pro nouzová volání, funkce úspory energie jako Power Saving Mode (PSM) a rozšířený idle mode DRX (eDRX) a vylepšené pokrytí pro IoT zařízení (CE mode). S 5G byl protokol NAS přepracován, aby byl modulárnější a dopředně kompatibilní, s podporou síťového řezání (network slicing), alternativních autentizačních metod a bezproblémové spolupráce mezi 3GPP a ne-3GPP přístupy (např. Wi-Fi). Vrstva NAS tedy není jen umožňovatelem konektivity, ale flexibilním rámcem, který se přizpůsobuje novým požadavkům služeb a síťovým paradigmatům definovaným v releasích 3GPP.

## K čemu slouží

Non-Access Stratum byl vytvořen za účelem zavedení jasného, standardizovaného a na přístupu nezávislého signalizačního protokolu mezi mobilním zařízením a jádrem sítě. Před jeho formální definicí v 3GPP měly rané celulární systémy monolitičtější a na technologii závislou řídicí signalizaci. Rozvrstvení na Access Stratum a Non-Access Stratum, koncept upevněný u GSM a plně realizovaný v UMTS, bylo klíčovým architektonickým rozhodnutím. Oddělilo rádiově specifické řídicí funkce (zpracovávané v AS sítí RAN) od funkcí správy účastníka a spojení (zpracovávaných v NAS sítí CN). Toto oddělení vyřešilo kritické problémy síťové evoluce a interoperability mezi více dodavateli.

Primární motivací bylo umožnit, aby se služby jádra sítě vyvíjely nezávisle na rádiovém rozhraní. Operátor sítě mohl upgradovat své jádro sítě na podporu nových služeb (např. hlasu založeného na IMS), aniž by vyžadoval změny na každé základnové stanici, pokud AS dokázalo nové zprávy NAS transparentně přenášet. Naopak, nové rádiové technologie (např. přechod z GSM na UMTS a LTE) mohly být zavedeny bez zásadní změny postupů jádra sítě pro autentizaci uživatele nebo zřizování datové relace. To výrazně snížilo složitost a náklady na modernizaci sítě. Také to usnadnilo bezproblémovou mobilitu a kontinuitu služeb při pohybu zařízení mezi různými technologiemi rádiového přístupu (inter-RAT mobilita), protože kontext NAS mohl být zachován a přenesen mezi uzly jádra sítě.

Dále NAS poskytuje zabezpečený, důvěryhodný koncový bod pro správu účastníků. Tím, že končí v jádru sítě, umožňuje centralizovanou autentizaci, autorizaci a správu klíčů. Bezpečnostní kontext vytvořený pomocí protokolů NAS (jako AKA) se používá k ochraně jak samotné signalizace NAS, tak dat uživatelské roviny. Tato architektura řeší omezení spočívající v distribuci kritických bezpečnostních funkcí nebo jejich závislosti na potenciálně méně důvěryhodné rádiové přístupové síti. Stručně řečeno, NAS existuje proto, aby poskytl stabilní, bezpečný a budoucím potřebám odolný základ řídicí roviny, který odděluje logiku služeb od přístupové technologie, a umožňuje tak škálovatelné a flexibilní mobilní sítě, jaké máme dnes.

## Klíčové vlastnosti

- Nezávislost na Access Stratum, umožňující provoz přes LTE, NR a ne-3GPP přístup
- Koncová ochrana integrity a šifrování mezi UE a jádrem sítě
- Správa mobility pro registraci, aktualizaci oblasti sledování a vyvolávání
- Správa relací pro zřizování, modifikaci a uvolňování PDU relací/přenosových kanálů
- Podpora výběru a vyjednávání síťového řezání (network slicing) v 5GS
- Mechanismy pro úsporu energie (PSM, eDRX) a vylepšené pokrytí pro IoT

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 23.236** (Rel-19) — Intra Domain Connection of RAN Nodes to Multiple CN Nodes
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 24.171** (Rel-19) — NAS Protocol for LCS in E-UTRAN
- **TS 24.206** (Rel-7) — Voice Call Continuity Between CS and IMS
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol
- **TS 24.368** (Rel-19) — NAS Configuration Management Object
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.543** (Rel-19) — SEAL Data Delivery Management Protocol
- **TS 24.558** (Rel-19) — Edge Enabler APIs Stage 3
- **TS 24.571** (Rel-19) — Control Plane LCS Procedures
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- … a dalších 52 specifikací

---

📖 **Anglický originál a plná specifikace:** [NAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/nas/)
