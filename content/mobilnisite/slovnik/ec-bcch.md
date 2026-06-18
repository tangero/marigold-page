---
slug: "ec-bcch"
url: "/mobilnisite/slovnik/ec-bcch/"
type: "slovnik"
title: "EC-BCCH – Extended Coverage BroadCast CHannel"
date: 2025-01-01
abbr: "EC-BCCH"
fullName: "Extended Coverage BroadCast CHannel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ec-bcch/"
summary: "Vylepšený vysílací kanál v sítích GSM/EDGE pro provoz v režimu rozšířeného pokrytí (Extended Coverage, EC). Vysílá základní systémové informace všem mobilním stanicím v buňce, včetně těch v hlubokém p"
---

EC-BCCH je vylepšený vysílací kanál v sítích GSM/EDGE, který vysílá základní systémové informace všem mobilním stanicím, včetně zařízení IoT v oblastech s hlubokým pokrytím nebo špatnými signálovými podmínkami.

## Popis

EC-BCCH (Extended Coverage Broadcast CHannel) je downlink logický kanál v GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiové přístupové síti ([GERAN](/mobilnisite/slovnik/geran/)), standardizovaný v 3GPP TS 44.060. Jedná se o variantu standardního vysílacího řídicího kanálu (Broadcast Control Channel, [BCCH](/mobilnisite/slovnik/bcch/)) pro rozšířené pokrytí. Jeho základní úlohou je vysílat klíčové systémové informace všem mobilním stanicím ([MS](/mobilnisite/slovnik/ms/)) v pokrytí buňky, se specifickými optimalizacemi zajišťujícími, že tyto informace dorazí i k zařízením pracujícím v náročných rádiových prostředích, pro která je určen EC-GSM-IoT. Kanál vysílá sadu zpráv systémových informací (System Information, [SI](/mobilnisite/slovnik/si/)), které obsahují parametry nezbytné pro to, aby si MS mohlo síť vybrat, synchronizovat se s ní a získat k ní přístup.

Z architektonického hlediska je EC-BCCH logický kanál mapovaný na specifické fyzické časové sloty. Klíčovým provozním rozdílem oproti standardnímu BCCH je použití masivního opakovacího kódování. Pro dosažení požadovaného rozšíření pokrytí (až o dalších 20 dB útlumu na spojení) je každý blok systémových informací na EC-BCCH opakovaně vysílán po dlouhou dobu, která pokrývá mnoho multirámců. Zařízení, které se chce v [EC](/mobilnisite/slovnik/ec/) režimu připojit k síti, musí tyto opakované přenosy monitorovat a akumulovat. Díky časové kombinaci signálu může zařízení systémové informace úspěšně dekódovat, i když okamžitý poměr signálu k šumu je výrazně pod prahem vyžadovaným pro normální provoz GSM.

Obsah vysílaný na EC-BCCH zahrnuje základní parametry, jako je globální identita buňky, dostupné rádiové zdroje, parametry řízení přístupu (např. pro [EC-RACH](/mobilnisite/slovnik/ec-rach/)) a plánovací informace pro další [EC](/mobilnisite/slovnik/ece-c/) kanály, jako je EC-CCCH. Může také vysílat specifické informace související s provozem EC-GSM-IoT. Tím, že zajišťuje robustní doručení těchto základních dat, umožňuje EC-BCCH zařízení IoT provést výběr buňky, vyhodnotit její vhodnost a zjistit, jak následně získat přístup k síti prostřednictvím EC-CCCH. Je prvním kontaktním bodem pro zařízení zapínající se v oblasti hlubokého pokrytí, což činí jeho spolehlivost klíčovou pro funkčnost celého systému EC-GSM-IoT.

## K čemu slouží

EC-BCCH byl vyvinut, aby vyřešil základní výzvu při nasazování celulárního IoT: poskytnout spolehlivé vysílané systémové informace zařízením v místech se silným útlumem signálu. Standardní přenosy GSM BCCH nebyly navrženy pro extrémní cíle pokrytí IoT aplikací, jako jsou chytré měřiče nebo senzory na stíněných místech. Bez přijetí systémových informací se zařízení nemůže synchronizovat se sítí ani zjistit pravidla pro přístup k ní, a je tedy nefunkční.

Jeho vytvoření bylo motivováno potřebou rozšířit dosah celulárních sítí pro hromadnou komunikaci mezi stroji (massive machine-type communications) bez nutnosti nového spektra nebo zcela nové rádiové přístupové technologie. Vylepšením stávajícího BCCH pomocí opakování řeší EC-BCCH problém 'prvního kontaktu'. Zajišťuje, že zařízení, bez ohledu na to, jak špatné je jeho rádiové spojení, může nakonec získat identitu a konfiguraci sítě. Toto zpětně kompatibilní vylepšení umožňuje síťovým operátorům upgradovat stávající GSM infrastrukturu pro podporu IoT, čímž poskytuje jasnou migrační cestu a využívá rozšířené nasazení GSM k efektivnímu poskytování služeb IoT s hlubokým pokrytím.

## Klíčové vlastnosti

- Vysílá zprávy systémových informací (System Information, SI) nezbytné pro přístup k síti v EC režimu
- Používá masivní opakování v časové oblasti pro extrémní vylepšení pokrytí
- Umožňuje výběr a převýběr buňky pro zařízení EC-GSM-IoT
- Poskytuje plánovací informace pro další EC řídicí kanály (EC-CCCH)
- Funguje jako trvale aktivní downlink logický kanál v buňce
- Základní pro počáteční synchronizaci zařízení ve scénářích hlubokého pokrytí

## Související pojmy

- [BCCH – Broadcast Control Channel](/mobilnisite/slovnik/bcch/)
- [EC-CCCH – Extended Coverage Common Control CHannel](/mobilnisite/slovnik/ec-ccch/)

## Definující specifikace

- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [EC-BCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ec-bcch/)
