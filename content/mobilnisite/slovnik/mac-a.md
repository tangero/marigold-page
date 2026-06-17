---
slug: "mac-a"
url: "/mobilnisite/slovnik/mac-a/"
type: "slovnik"
title: "MAC-A – Message Authentication Code for Authentication"
date: 2025-01-01
abbr: "MAC-A"
fullName: "Message Authentication Code for Authentication"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/mac-a/"
summary: "Kryptografický kód pro ověření zprávy (MAC) používaný v protokolu 3GPP Authentication and Key Agreement (AKA). Ověřuje pravost výzev k autentizaci vyměňovaných mezi sítí a uživatelským zařízením (UE),"
---

MAC-A je kód pro ověření zprávy (Message Authentication Code) používaný v protokolu 3GPP AKA k ověření pravosti výzvy k autentizaci mezi sítí a uživatelským zařízením (UE) a k zabránění zneužití identity.

## Popis

MAC-A je klíčová kryptografická součást procedury 3GPP Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)), standardizované od vydání Release 8. Funguje jako kód pro ověření zprávy (Message Authentication Code), což je krátký informační blok vygenerovaný pomocí kryptografického algoritmu a tajného klíče k ověření pravosti a integrity zprávy. V kontextu AKA je MAC-A konkrétně generován na straně sítě (typicky v autentizačním centru, AuC, uvnitř Home Subscriber Server, [HSS](/mobilnisite/slovnik/hss/)) a je zahrnut v autentizačním vektoru ([AV](/mobilnisite/slovnik/av/)) odeslaném do obslužné sítě (např. [MME](/mobilnisite/slovnik/mme/) v EPS, [AMF](/mobilnisite/slovnik/amf/) v 5GS). Tento AV obsahuje parametry jako RAND (náhodná výzva), [AUTN](/mobilnisite/slovnik/autn/) (autentizační token), XRES (očekávaná odpověď) a relací klíče.

Samotný AUTN (Authentication Token) je konstruovaný parametr, který mimo jiné obsahuje MAC-A. Když UE obdrží autentizační výzvu (RAND a AUTN), nezávisle spočítá svou vlastní verzi MAC-A pomocí sdíleného tajného klíče K (uloženého na USIM a v AuC), přijatého RAND a dalších parametrů, jako je číslo sekvence (SQN). UE následně porovná svůj vypočítaný MAC-A s tím, který extrahuje z přijatého AUTN. Pokud se shodují, UE kryptograficky ověřilo, že autentizační výzva pochází od skutečné síťové entity disponující správným sdíleným tajemstvím K. Tento krok vzájemné autentizace je zásadní pro navázání důvěry před zahájením jakékoli relace uživatelských dat.

Z architektonického hlediska jsou generování a ověření MAC-A rozděleny mezi autentizační infrastrukturu jádra sítě (HSS/AuC) a aplikaci USIM na kartě UICC v UE. K výpočtu MAC-A se používá algoritmus MILENAGE, jak je specifikováno v 3GPP TS 35.205 a 35.909, který je založen na blokové šifře [AES](/mobilnisite/slovnik/aes/) (Advanced Encryption Standard). Konkrétní vstupy funkce MAC-A zahrnují tajný klíč K, náhodnou výzvu RAND a číslo sekvence SQN, což zajišťuje, že každý pokus o autentizaci vytvoří jedinečný, neopakovatelný [MAC](/mobilnisite/slovnik/mac/). Jeho role je čistě pro autentizaci sítě z pohledu UE; neposkytuje integritu uživatelských datových přenosů, které jsou zajištěny samostatnými klíči a mechanismy, jako je MAC-I.

Bezpečnost celého protokolu AKA závisí na robustnosti MAC-A. Selhání při ověření MAC-A na straně UE vede k zamítnutí autentizace, což chrání uživatele před připojením k nelegitimním základnovým stanicím nebo sítím, které se snaží zachytit komunikaci. Je to kritický prvek řetězce důvěry, který je základem bezpečnosti mobilních sítí a umožňuje služby od základních hovorů až po transakce s vysokou hodnotou přes mobilní připojení.

## K čemu slouží

MAC-A byl zaveden, aby poskytl standardizovaný, kryptograficky silný mechanismus pro autentizaci sítě vůči UE v rámci 3GPP AKA. Před sjednoceným AKA v 3GPP měly starší mobilní systémy různé autentizační metody, které často postrádaly robustní vzájemnou autentizaci a procedury odvozování klíčů potřebné pro rozvíjející se paketové služby a rostoucí hrozby. Hlavní problém, který MAC-A řeší, je zneužití identity sítě, kdy by se škodlivá entita mohla pokusit vydávat za legitimní operátorskou síť za účelem získání uživatelských přihlašovacích údajů nebo spuštění útoku typu man-in-the-middle.

Jeho vytvoření bylo motivováno potřebou nové, algoritmicky flexibilní bezpečnostní architektury pro EPS (LTE) a následné systémy, která by se vzdálila od algoritmů COMP128 používaných ve 2G/3G. Skupina 3GPP TSG SA WG3 (Security group) specifikovala MILENAGE jako příkladní sadu algoritmů, přičemž MAC-A je její klíčovou funkcí. To umožnilo vzájemnou autentizaci: zatímco síť autentizuje UE prostřednictvím kontroly RES/XRES, UE autentizuje síť prostřednictvím kontroly MAC-A uvnitř AUTN. Toto vzájemné ověření vytváří oboustranný vztah důvěry, který je nezbytný pro zabezpečené poskytování služeb.

Navíc je návrh MAC-A jako součásti komplexní hierarchie klíčů podporuje odvození více následných kryptografických klíčů (CK, IK, Kasme) pro šifrování a ochranu integrity přenosů jak řídicí, tak uživatelské roviny. Řeší omezení předchozích přístupů tím, že je transparentně implementovatelný na kartách USIM, což umožňuje zpětnou kompatibilitu a hladkou migraci, a zároveň poskytuje základ, který měl být odolný vůči kryptografickým útokům v dohledné budoucnosti.

## Klíčové vlastnosti

- Používá se konkrétně pro autentizaci sítě vůči UE v rámci protokolu AKA.
- Generován síťovým AuC/HSS a ověřován USIM v UE.
- Vypočítáván pomocí sady algoritmů MILENAGE založené na AES.
- Vstupy zahrnují sdílený tajný klíč K, náhodnou výzvu RAND a číslo sekvence SQN.
- Vložen do autentizačního tokenu (AUTN) odesílaného do UE.
- Selhání při ověření způsobí okamžité zamítnutí autentizace a blokuje připojení k nedůvěryhodným sítím.

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [AUTN – Authentication Token](/mobilnisite/slovnik/autn/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [MAC-I – Message Authentication Code for Integrity](/mobilnisite/slovnik/mac-i/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 33.105** (Rel-19) — 3G Security: Cryptographic Algorithm Requirements
- **TS 35.205** (Rel-19) — MILENAGE Algorithm Set: General Overview
- **TR 35.909** (Rel-19) — 3GPP MILENAGE Algorithm Design Report
- **TR 35.934** (Rel-19) — Tuak algorithm set for 3GPP auth & key gen

---

📖 **Anglický originál a plná specifikace:** [MAC-A na 3GPP Explorer](https://3gpp-explorer.com/glossary/mac-a/)
